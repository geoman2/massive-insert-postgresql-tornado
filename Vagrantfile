# -*- mode: ruby -*-
# vi: set ft=ruby ts=2 sw=2 expandtab :
PROJECT = "massive_insert_postgresql_tornado"
PROJECT_DIRECTORY = "/home/vagrant"
UID = Process.euid
DB_USER = "vagrant"
DB_PASSWORD = "vagrant"
DB_HOST = "db"
DB_NAME = "vagrant"

DOCKER_ENV = {
  "PROJECT_DIRECTORY" => "#{PROJECT_DIRECTORY}",
  "APP_PATH" => "#{PROJECT_DIRECTORY}/massive_insert_postgresql_tornado",
}

Vagrant.configure(2) do |config|
  config.vm.define "db" do |app|
    app.vm.provider "docker" do |d|
      d.image = "postgres:9.6"
      d.name = "#{PROJECT}_db"
      d.env = {
        "POSTGRES_PASSWORD" => DB_PASSWORD,
        "POSTGRES_USER" => DB_USER,
        "POSTGRES_DB" => DB_NAME,
      }
    end
  end
  config.vm.define "dev" do |app|
    app.vm.provider "docker" do |d|
      d.image = "allansimon/allan-docker-dev-python"
      d.name = "#{PROJECT}_dev"
      d.link "#{PROJECT}_db:db"
      d.volumes =  [
        "#{ENV['PWD']}/:#{PROJECT_DIRECTORY}"
      ]
      d.env = {
        'HOST_USER_UID' => UID,
        'DB_USER' => DB_USER,
        'DB_PASSWORD' => DB_PASSWORD,
        'DB_HOST' => DB_HOST,
        'DB_NAME' => DB_NAME,
        # when doing vagrant ssh, you will be automatically
        # put in that directory
        'PROJECT_DIRECTORY' => "#{PROJECT_DIRECTORY}"
      }
      d.has_ssh = true
    end

    # forward Locust port for host web browser usage
    app.vm.network "forwarded_port", guest: 8089, host: 8089

    app.vm.provision "ansible", type: "shell" do |ansible|
      ansible.env = DOCKER_ENV
      ansible.inline = "
        set -e
        cd $APP_PATH
        ansible-playbook provisioning/bootstrap-dev.yml
        echo 'done, you can now run `vagrant ssh`'
      "
    end
  end
end
