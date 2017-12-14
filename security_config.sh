#/bin/bash

echo "Beginning security baseline configuration..."

sshvar=0

##disable null passwords
sudo grep "nullok" /etc/pam.d/system-auth-ac > /dev/null 2>&1; RC=${?}
if [ ${RC} -eq 0 ]
then
   echo "nullok is set...removing null password option."
   sudo  sed -i 's/\<nullok\>//g' /etc/pam.d/system-auth
   sudo  sed -i 's/\<nullok\>//g' /etc/pam.d/system-auth-ac
fi   

##disable ssh root login
sudo grep "PermitRootLogin yes" /etc/ssh/sshd_config > /dev/null 2>&1; RC=${?}
if [ ${RC} -eq 0 ]
then
   echo "PermitRootLogin is set to yes...disabling ssh root login."
   sudo sed -i s/"#PermitRootLogin yes"/"PermitRootLogin no"/g /etc/ssh/sshd_config
   let "sshvar++"
fi

##disable ssh login with empty password
sudo grep "PermitEmptyPasswords yes" /etc/ssh/sshd_config > /dev/null 2>&1; RC=${?}
if [ ${RC} -eq 0 ]
then
   echo "PermitEmptyPasswords is set to yes...disabling ssh login with empty password."
   sudo sed -i s/"#PermitEmptyPasswords yes"/"PermitEmptyPasswords no"/g /etc/ssh/sshd_config
   sudo sed -i s/"PermitEmptyPasswords yes"/"PermitEmptyPasswords no"/g /etc/ssh/sshd_config
   let "sshvar++"
fi

if [ ${sshvar} -gt 0 ]
then
   echo "Restarting the sshd daeomon..."
   sudo /sbin/service sshd restart
fi

##remove special privileged users halt and shutdown
sudo userdel -f halt
sudo userdel -f shutdown

echo "Security baseline configuration complete!"
