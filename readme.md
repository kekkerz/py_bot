# Py_Bot


Py_bot is a chat moderation bot made to be used with twitch.tv and was written in Python 3.4.

This bot is still very early in development and currently only responds to a few commands.

## List of commands:

```
!hi - Bot responds to the user in chat saying "@<username> Hello!".

!add_command <command_name> "Text" - Allows a moderator of the chat room to add a custom command for users to run. For example, on a speedrun channel, you may want to add a command called "!run" and have the bot respond to the user with information about the run.

!remove_command <command_name> - Allows moderator to remove custom commands that were previously added.
        
!quit - Allows the broadcaster to close the bot remotely.
```

## To do list:

1. Add `!update_command` that allows moderator to update existing custom commands, rather than needing to remove, and re-add.

2. Add a `!raffle_start` command to allow broadcaster to start a raffle for giveaways. Users will type `!raffle` to enter.

3. Add moderation functionality where the bot will be able to timeout users based on content contained in their messages.

4. Add ability to log chat activity to a file.
