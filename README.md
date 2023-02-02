# raspberry-pipewire-speaker
Configuration files to make a modern bluetooth/spotify connect speaker using Pipewire out of a Raspberry pi.

## Goal of this project

List the configuration steps I had to go through / files I needed to configure in order to make a Bluetooth sink / Spotify Connect receiver out of a raspberry pi (or in my case, a chinese Android box using a custom Armbian build).

Requirements I had:
- Support Spotify connect (with a recent, maintained project)
- Support Bluetooth audio as a sink (with low-enough latency for video playback, and optionally with more codecs than just SBC)
- Use a modern audio backend. I started this project using raspotify (with alsa backend) and bluez-alsa. This allowed for bit-perfect output but I started to have erratic behaviour when switching audio streams (distorded audio, high bluetooth latency). That was often solved restarting components
- Minimal maintenance required. Plug device and forget it.
- Audio quality is a target, but I gladly trade bit-perfectness to stability with good-enough quality resampling. I wasn't able to find any difference in critical listening, and even less so in day-to-day casual listening.

Alsa was out (because too fragile when abused, and using dmix made bluetooth latency shoot up), and as Pipewire seems to be replacing PulseAudio it was making sense to investigate researching setting it up.

## 1. Install & configure Pipewire/Wireplumber

Tested using debian & ubuntu, installation steps are similar (//TODO add link, google is your friend). You need to install pipewire, pipewire-pulse & wireplumber

//TODO add instructions to override default resampling rate/quality in pipewire-pulse.conf

## 2. Build, install & configure librespot

It seems the most active Spotify Connect implementation, and supports pulseaudio backend (so it can talk to pipewire almost natively). Build & installation instructions are on the Librespot repo (//TODO add link). I use the `v0.4.2` release as it was the last one using the 'old' api (and work on the 'new' api was a bit fresh at time of writing).

//TODO add link to systemd user configuration example

## 3. Configure Bluez

//TODO

## 4. Enable user lingering + Auto tty login

So at boot time, user session is started and everything gets loaded
//TODO

## 5. (Optional) Integrate with MQTT (so can be controlled through Home Assistant, for example)

//TODO
