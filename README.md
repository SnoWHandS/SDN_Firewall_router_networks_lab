# eee4121f-b-lab2

Labs for EEE4121F-B

Dillon Heald - HLDDIL001

# Part 1
Simply execute "runPart1.sh" by "sudo ./runPart1.sh". This will execute both pox and mininet and automatically perform a pingall. When the pingall is complete the script cleans up processes in the background and resets mininet.
Note: This will copy all the firewall policies in the firewall-policies.csv file found in firewall and apply the l2 learning changes.

# Part 2
To execute part 2 of lab 2, run the "runPart2.sh" script using "sudo ./runPart2.sh". This will run the simulation and upon closing the mininet terminal, stop the mininet background session.

Once mininet is running, simply type "pingall" to show end to end connectivity.

Type exit to close the mininet terminal

Note: If you didn't execute the program with the "runPart2.sh" bash script, the following applies:
Once back at the bash terminal run "make stop" to close the background mininet process if you didn't run "runPart2.sh".

If you wish to clean the directory, type "make clean" to clear the directory of all captures and logs.
