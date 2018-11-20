REM https://www.spigotmc.org/threads/useful-java-arguments-to-increase-server-performance.98374/
@echo off
java -server -XX:-UseAdaptiveSizePolicy -Xms2G -Xmx2G -XX:+AlwaysPreTouch -XX:+DisableExplicitGC -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=4M -XX:TargetSurvivorRatio=90 -XX:G1NewSizePercent=50 -XX:G1MaxNewSizePercent=80 -XX:InitiatingHeapOccupancyPercent=10 -XX:G1MixedGCLiveThresholdPercent=50 -XX:+AggressiveOpts -jar minecraft_server.1.13.2.jar nogui
pause
