# TODO: Add link to original script

# input validator and help
case "$1" in
	install_alpine)
	    DOCKERIMAGE=http://dl-cdn.alpinelinux.org/alpine/v3.6/releases/armhf/alpine-minirootfs-3.6.2-armhf.tar.gz
	    ;;
	uninstall)
        chmod -R 777 ~/alpine
	    rm -rf ~/alpine
	    rm -f /data/data/com.termux/files/usr/bin/startalpine
	    hash -r
	    exit 0
	    ;;
	*)
	    echo $"Usage: $0 {install_alpine|uninstall}"
	    exit 2
	    ;;
esac


# install necessary packages
apt update
apt install wget proot xz-utils tar -y
hash -r

# get the docker image
mkdir ~/alpine
cd ~/alpine
wget $DOCKERIMAGE -O alpine.tar.xz

# extract the Docker image
tar xpvf alpine.tar.xz

# cleanup
chmod +w .
rm alpine.tar.xz

# fix DNS
echo "nameserver 8.8.8.8" > ~/alpine/etc/resolv.conf

# make a shortcut
cat > /data/data/com.termux/files/usr/bin/startalpine <<- EOM
#!/data/data/com.termux/files/usr/bin/bash
proot --link2symlink -0 -r ~/alpine -b /dev/ -b /sys/ -b /proc/ -w /root /usr/bin/env -i HOME=/root TERM="xterm-256color" PS1='[termux@alpine \W]$ ' LANG=en_US.UTF-8 PATH=/bin:/usr/bin:/sbin:/usr/sbin DISPLAY=:0 /bin/ash --login
EOM

chmod +x /data/data/com.termux/files/usr/bin/startalpine

# all done
echo "All done! Start Alpine 3.6 with 'startalpine'."
