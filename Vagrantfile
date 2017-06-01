# -*- mode: ruby -*-
# vi: set ft=ruby ts=2 sw=2 expandtab :

# used for 'dev' containers to have same permissions as current user
UID = Process.euid
PROJECT_DIR="/vagrant"
VIRTUAL_ENV_PATH="/tmp/virtual_env35"
TARGET="dev"
TORNADO_PORT="8080"
PROJECT = "massive-insert-postgresql-tornado"
DB_USER = "vagrant"
DB_PASSWORD = "vagrant"
DB_HOST = "db"
DB_NAME = "vagrant"

ENV['VAGRANT_NO_PARALLEL'] = 'yes'
ENV['VAGRANT_DEFAULT_PROVIDER'] = 'docker'
VAGRANTFILE_VERSION = "2"
Vagrant.configure(VAGRANTFILE_VERSION) do |config|

  environment_variables = {
    "HOST_USER_UID" => UID,
    "TARGET" => TARGET,
    "ENV_NAME" => "devdocker",
    "APP_PATH" => PROJECT_DIR,
    "VIRTUAL_ENV_PATH" => VIRTUAL_ENV_PATH,
    "PROJECT" => PROJECT,
    "TORNADO_PORT" => TORNADO_PORT,
    "DB_USER" => DB_USER,
    "DB_PASSWORD" => DB_PASSWORD,
    "DB_HOST" => DB_HOST,
    "DB_NAME" => DB_NAME,
  }

  config.vm.define "db" do |app|
    app.vm.provider "docker" do |d|
      d.image = "postgres:9.4"
      d.name = "#{PROJECT}_db"
      d.env = {
        "POSTGRES_PASSWORD" => DB_PASSWORD,
        "POSTGRES_USER" => DB_USER,
        "POSTGRES_DB" => DB_NAME,
      }
    end
  end

  config.ssh.insert_key = true
  config.vm.define "dev", primary: true do |app|
    app.vm.provider "docker" do |d|
      d.image = "allansimon/allan-docker-dev-python"
      d.name = "#{PROJECT}_dev"
      d.has_ssh = true
      d.env = environment_variables
    end
    app.ssh.username = "vagrant"

    # forward Locust port for host web browser usage
    app.vm.network "forwarded_port", guest: 8080, host: 8080

    app.vm.provision "ansible", type: "shell" do |ansible|
      ansible.env = environment_variables
      ansible.inline = "
        set -e
        cd $APP_PATH
        ansible-playbook provisioning/bootstrap.yml
        echo 'done, you can now run `vagrant ssh`'
      "
    end
  end
end
