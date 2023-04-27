# Welcome to Heroes of the Fallen Kingdom - HOTFK -

## Changelog

### v. <span style="color:pink">experimental<span> <span style="color:white"> 0.0.13b <span> <span style="color:pink">28/Apr/2023<span>

    Different route for major experiments

 The following changes can be found under the `rebased` folder:

 - Updated Discord Activity to extract User avatar, username and discriminant
 - Added detection of requests for Invite or Join trough Discord Activity.
 - Improved GUI with dynamic positioning, scaling and scene fading effects.
 - New widgets for displaying text on screen including multiple lines.
 - New class for discord RPC activity and the required methods.
 - <span style="color:red"> game maps are currently disabled for debugging and implementing new features.<span>

---

### v. pre 0.0.13a <span style="color:grey">27/Apr/2023<span>

    The experiments continue...

 - 2 New Scenes to debug collisions and player movement.
 - New Entity class to derive players and other entities.
 - Small changes for menu GUIs

---

<details closed>
<summary><span style="color:grey">Older Releases</span></summary>

### v. pre 0.0.12a <span style="color:grey">24/Apr/2023<span>

    You've got to experiment to figure out what works. (And fail a lot...)

 - Tilemap experiment.
 - Collisions experiment.
 - Player and movement experiment.

### v. pre 0.0.11a <span style="color:grey">23/Apr/2023<span>
 - New fonts for the game.
 - Option to toggle chat/console visibility.
 - New sandbox area (will be used for debugging mostly).
 - Notification widget to dispaly text on screen.
 - Modified the structe and the way that the game loads components.
 - Added Scenes and Camera with the posibility to follow an Object or Entity.

### v. pre 0.0.10a <span style="color:grey">18/Apr/2023</span>
    Settings Update! Everything is loaded and saved with dynamic configuration file!
 - Settings are now automatically loaded.
 - Options to save or reset settings.

### v. pre 0.0.9a <span style="color:grey">17/Apr/2023</span>
 - Implemented Discord SDK for activity status and party management.
 - Polishing things up before first content update!
 - Made the code more readable and removed obsolete parts.
 - Added a few console commands to controll music and sfx.
 - Started to work on Options (INCOMPLETE).

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

### **when the command finishes, copy the `resources` and `lib` folder to the installation path (in the same directory as the game executable)**

## Contact
### Discord or email
Send meus a direct message at `Rioter Neeko#0646` or join me using [this server invite](https://discord.gg/xcEYBpn2k2).

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
- [x] Discord Party (join / invite)
- [x] Fix in-game Disclaimer
- [x] Finish Options settings
<details closed>
<summary><span style="color:grey">View All</span></summary>
- [x] Sound System
- [x] Core System
- [x] Menu Views
- [x] Chat System
- [x] Uninterupted music between scenes
- [x] Responsive GUI
- [x] Animated Main Menu
- [x] Discord SDK implemented
- [X] Rework Font System
- [x] Creative / Sandbox
- [x] Commands to support Creative / Sandbox
- [x] Save and Load data
- [x] Tutorial level (Singleplayer)
</details>

### Next
- [ ] Notifications System
- [ ] Fix button collisions
- [ ] Co-op playing

### Future
- [ ] Cloud saving
- [ ] Player, Enemy, AI
- [ ] Player inventory
- [ ] Account management
- [ ] Co-Op (max 4 extra friends)
- [ ] Multiplayer

> More mechanics and features to be announced!
