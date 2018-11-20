REM https://www.spigotmc.org/threads/useful-java-arguments-to-increase-server-performance.98374/
@echo off
java -server -XX:-UseAdaptiveSizePolicy -Xms2G -Xmx2G -XX:+AlwaysPreTouch -XX:+DisableExplicitGC -XX:+UseG1GC -XX:+AggressiveOpts -jar minecraft_server.1.13.2.jar nogui
pause
