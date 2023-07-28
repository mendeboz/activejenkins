def gitClone = "git clone https://github.com/mendeboz/activejenkins.git /home/vagrant/git/activejenkins"
println(gitClone)
gitClone.execute();
// gitClone.waitForOrKill(100)
        
def gitUpdate = "git -C /home/vagrant/git/activejenkins pull".execute();
// gitUpdate.waitForOrKill(100)
        
def gitCheckout = "git -C /home/vagrant/git/activejenkins checkout master".execute(); 
// gitCheckout.waitForOrKill(100) 

def list = ['/bin/sh', '-c', "sed -n ' /\\[dnsmasq]/ , /\\[/ {/\\[/!p} ' /home/vagrant/git/activejenkins/hosts.ini"]
list= list.execute().text.split('\n');




println (list.flatten())