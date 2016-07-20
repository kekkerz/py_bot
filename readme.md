# Py_Bot


Py_bot is a chat moderation bot made to be used with twitch.tv and was written in Python 3.4.

This bot is still very early in development and currently only responds to a few commands.

## List of commands:

```
!hi - Bot responds to the user in chat saying "@<username> Hello!".

!add_command <command_name> "Text" - Allows a moderator of the chat room to add a custom command for users to run. For example, on a speedrun channel, you may want to add a command called "!run" and have the bot respond to the user with information about the run.

!update_command <command_name> "New Text" - Update an existing custom command, rather than needing to remove, and re-add.

!remove_command <command_name> - Allows moderator to remove custom commands that were previously added.

!raffle_start - Broadcaster can use this command to start a raffle for giveaways. Users use !raffle to enter.

!raffle - If a raffle is in progress, users can use this command to enter the raffle. Only one entry is allowed.

!raffle_end - Used by broadcaster to end raffle. This command will select a winner from a list of users that used !raffle and will then end the raffle.
        
!quit - Allows the broadcaster to close the bot remotely.
```

## Logging chat activity to file.

By default, chat logs are placed in src/logs/'Current Date'.log. Modify src/config/config.py to change log location.

## To do list:

1. Add moderation functionality where the bot will be able to timeout users based on content contained in their messages.

## Changelog

07/17 Added !update_command, raffle functionality, and ability to log chat activity to a file.

07/19 Added command cooldowns, sub-only links, and additional config settings.

	log_dir - Specify a custom location for log files.

	sub_only_links - Enable/disable subscriber only links.

	link_timeout_message - Customize message sent to user when they are timed out for pasting a link.

	link_timeout_time - Duration for non-sub link timeouts.

	default_cmd_cd - The default cooldown time for commands.07/19 Added command cooldowns, sub-only links, and additional config settings.

	log_dir - Specify a custom location for log files.

	sub_only_links - Enable/disable subscriber only links.

	link_timeout_message - Customize message sent to user when they are timed out for pasting a link.

	link_timeout_time - Duration for non-sub link timeouts.

	default_cmd_cd - The default cooldown time for commands.07/19 Added command cooldowns, sub-only links, and additional config settings.

	log_dir - Specify a custom location for log files.

	sub_only_links - Enable/disable subscriber only links.

	link_timeout_message - Customize message sent to user when they are timed out for pasting a link.

	link_timeout_time - Duration for non-sub link timeouts.

	default_cmd_cd - The default cooldown time for commands.07/19 Added command cooldowns, sub-only links, and additional config settings.

	log_dir - Specify a custom location for log files.

	sub_only_links - Enable/disable subscriber only links.

	link_timeout_message - Customize message sent to user when they are timed out for pasting a link.

	link_timeout_time - Duration for non-sub link timeouts.

	default_cmd_cd - The default cooldown time for commands.07/19 Added command cooldowns, sub-only links, and additional config settings.

	log_dir - Specify a custom location for log files.

	sub_only_links - Enable/disable subscriber only links.

	link_timeout_message - Customize message sent to user when they are timed out for pasting a link.

	link_timeout_time - Duration for non-sub link timeouts.

	default_cmd_cd - The default cooldown time for commands.07/19 Added command cooldowns, sub-only links, and additional config settings.

	log_dir - Specify a custom location for log files.

	sub_only_links - Enable/disable subscriber only links.

	link_timeout_message - Customize message sent to user when they are timed out for pasting a link.

	link_timeout_time - Duration for non-sub link timeouts.

	default_cmd_cd - The default cooldown time for commands.07/19 Added command cooldowns, sub-only links, and additional config settings.

	log_dir - Specify a custom location for log files.

	sub_only_links - Enable/disable subscriber only links.

	link_timeout_message - Customize message sent to user when they are timed out for pasting a link.

	link_timeout_time - Duration for non-sub link timeouts.

	default_cmd_cd - The default cooldown time for commands.
