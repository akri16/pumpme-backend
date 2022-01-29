#!/bin/bash

JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
link=$1
name=$2

dir=$(realpath $(dirname $0))
echo $dir

if [[ -z $link ]] || [[ -z $name ]]; then
	exit 1
fi

name=$name.apk
mkdir $dir/../repo
git clone $link $dir/../repo 
cd $dir/../repo
cp ../local.properties .
chmod +x gradlew
./gradlew assembleDebug 
cd ..
cp repo/app/build/outputs/apk/debug/app-debug.apk output/$name
chmod 777 repo
rm -f -r repo
echo $name 



