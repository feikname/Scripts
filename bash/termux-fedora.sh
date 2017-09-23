# TODO: Add link to original script

# input validator and help
case "$1" in
	f26_arm)
	    DOCKERIMAGE=http://download.fedoraproject.org/pub/fedora/linux/releases/26/Docker/armhfp/images/Fedora-Docker-Base-26-1.5.armhfp.tar.xz
	    ;;
	f26_arm64)
	    DOCKERIMAGE=https://download.fedoraproject.org/pub/fedora-secondary/releases/26/Docker/aarch64/images/Fedora-Docker-Base-26-1.5.aarch64.tar.xz
	    ;;
	uninstall)
            chmod -R 777 ~/fedora
	    rm -rf ~/fedora
	    rm -f /data/data/com.termux/files/usr/bin/startfedora
	    hash -r
	    exit 0
	    ;;
	*)
	    echo $"Usage: $0 {f26_arm|f26_arm64|uninstall}"
	    exit 2
	    ;;
esac


# install necessary packages
apt update
apt install wget proot tar -y
hash -r

# get the docker image
mkdir ~/fedora
cd ~/fedora
wget $DOCKERIMAGE -O fedora.tar.xz

# extract the Docker image
tar xvf fedora.tar.xz --strip-components=1 --exclude json --exclude VERSION

# extract the rootfs
tar xpf layer.tar

# cleanup
chmod +w .
rm layer.tar
rm fedora.tar.xz

# fix DNS
echo "nameserver 8.8.8.8" > ~/fedora/etc/resolv.conf

# make a shortcut
cat > /data/data/com.termux/files/usr/bin/startfedora <<- EOM
#!/data/data/com.termux/files/usr/bin/bash
proot --link2symlink -0 -r ~/fedora -b /dev/ -b /sys/ -b /proc/ -w /root /bin/env -i HOME=/root TERM="$TERM" PS1='[termux@fedora \W]\$ ' LANG=$LANG PATH=/bin:/usr/bin:/sbin:/usr/sbin DISPLAY=:0 /bin/bash --login
EOM

chmod +x /data/data/com.termux/files/usr/bin/startfedora

# all done
echo "All done! Start Fedora with 'startfedora'. "
