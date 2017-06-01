# -*- mode: ruby -*-
# vi: set ft=ruby ts=2 sw=2 expandtab :

# used for 'dev' containers to have same permissions as current user
UID = Process.euid
PROJECT_DIR="/vagrant"
VIRTUAL_ENV_PATH="/tmp/virtual_env35"
TARGET="dev"
TORNADO_PORT="8080"
PROJECT = "massive-insert-postgresql-tornado"

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
  }

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
    app.vm.network "forwarded_port", guest: 8089, host: 8089

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
