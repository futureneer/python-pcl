# Vagrant 1.0.3

Vagrant::Config.run do |config|
  config.vm.box = "precise32"
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"

  config.vm.provision :shell, :path => "bootstrap.sh"

  #config.vm.network :hostonly, "192.168.50.5"

  #config.vm.boot_mode = :gui

end
