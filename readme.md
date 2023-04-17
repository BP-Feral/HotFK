# Welcome to Heroes of the Fallen Kingdom - HOTFK -

## Changelog

### v. pre 0.0.9a <span style="color:grey">17/Apr/2023</span>
 - Implemented Discord SDK for activity status and party management.
 - Polishing things up before first content update!
 - Made the code more readable and removed obsolete parts.
 - Added a few console commands to controll music and sfx.
 - Started to work on Options (INCOMPLETE).

<details closed>
<summary><span style="color:grey">Older Releases</span></summary>

### v. pre 0.0.8a <span style="color:grey">11/Apr/2023</span>
 - Created a global mixer for easier usage.
 - New options page.

### v. pre 0.0.7a <span style="color:grey">11/Apr/2023</span>
 - Added a chat box that will be used to chat or input commands later on.
 - Game no longer close completely when pressing Escape too many times.
 - Fixed invalid invite link for Discord server.

### v. pre-0.0.6a <span style="color:grey">9/Apr/2023</span>
- Added particles class and particles in the main menu.
- Added sound mixer for background music and putton events.
- Created 2 new buttons for options and leaving the game.
- Adjusted certain UI elements.

### v. pre-0.0.5a <span style="color:grey">4/Feb/2023</span>
- Added links for Discord and Github in the main menu
- Paralax background

### v. pre-0.0.4a <span style="color:grey">3/Feb/2023</span>
- Added 5 slots for offline accounts
- Started the accounts system

### v. pre-0.0.3a
- More files removed (some will return later)
- Better game-loop and events handling

### v. pre-0.0.2a
- Older backup files moved to cloud and now require a key to access.
- Cache removal for multiple folders.
- Other unused resources removed.
- Dynamic scaling to support different monitor resolutions.
- Adjusted certain files and code for the upcoming updateds.

</details>

## How to install

Currently there is no installation file, you have to compile a copy of the game on your own. To do that you need the following:

 - python 3.11.2 or higher installer
 - `pyinstaller` module installed using `pip install pyinstaller`

after that you have to run the following command in the project folder:

`pyinstaller main.py` this will create an executable for the game to run. 

if you need all the intended fancy stuff such as the name, no console and icon run the following command instead:

`pyinstaller main.py --name "Heroes of the Fallen Kingdom" --noconsole --icon "resources/images/icons/icon.ico"`


## Contact
### Discord or email
Send us a direct message at `Rioter Neeko#0646` / `Yserion#7716` or join us using [this server invite](https://discord.gg/xcEYBpn2k2).

You can also send me an email at mihai.pricbo@yahoo.com if DIscord is not an option.

## FaQ
When will it be released?
> TBD - There is no date for release yet, the core mechanics are still in development and it still require heavy investment.

I have a Suggestion or an Issue to report
> You can file a report using GitHub Issue Tickets or contact us directly using the information above.


## Disclaimer
[ **!** ] Since the game is in early development, things might take drastic turns as we try different approaches and see what might work and what not.

[ **!** ] Everything presented so far is subject to change. We ask for understandment and caution if you proceed in testing and supporting us.


## Wrapping things up
And finally, I repeat once again, if there is anything else let us know.
We will continue to work on further updates and a way to deliver a beta version as soon as possible.

## TODO
### Completed
- [x] Core System
- [x] Sound System
- [x] Menu Views
- [x] Chat System
- [x] Uninterupted music between scenes
- [x] Responsive GUI
- [x] Animated Main Menu
- [x] Discord SDK implemented

### Next
- [ ] Notifications System
- [ ] Fix in-game Disclaimer
- [ ] Fix button collisions
- [ ] Finish Options settings
- [ ] Discord Party (join / invite)
- [ ] Co-op playing

### Future
- [ ] Rework Font System
- [ ] Creative / Sandbox
- [ ] Commands to support Creative / Sandbox
- [ ] Save and Load data
- [ ] Cloud saving
- [ ] Player, Enemy, AI
- [ ] Player inventory
- [ ] Tutorial level (Singleplayer)
- [ ] Account management
- [ ] Co-Op (max 4 extra friends)
- [ ] Multiplayer

> More mechanics and features to be announced!
