REM https://www.minecraftforum.net/forums/archive/alpha/alpha-survival-multiplayer/823328-making-your-server-lag-less-by-tuning-java
@echo off
java -server -XX:-UseAdaptiveSizePolicy -Xms2G -Xmx2G -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -jar minecraft_server.1.13.2.jar nogui
pause
