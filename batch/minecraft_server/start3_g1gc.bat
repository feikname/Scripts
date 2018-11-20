REM https://www.reddit.com/r/feedthebeast/comments/5jhuk9/modded_mc_and_memory_usage_a_history_with_a/
@echo off
java -server -XX:-UseAdaptiveSizePolicy -XX:+UseG1GC -Xms2G -Xmx2G -Dsun.rmi.dgc.server.gcInterval=2147483646 -XX:+UnlockExperimentalVMOptions -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M -jar minecraft_server.1.13.2.jar nogui
pause
