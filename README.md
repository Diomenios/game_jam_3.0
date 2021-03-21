# Redneck Ramble

Developped with ❤️ by **C'était mieux avant**

## Installation

1. Clone this Github repository
2. TODO VENV ??
3. PIP INSTALL ??


## Utilisation

1. Open a terminal in `game_jam_3.0` folder.
2. Install virtualenv with pip for Python 3 : `pip install virtualenv` 
3. Launch a virtualenv : `virtualenv -p python3 env`
4. Activate virtualenv : `source env/bin/activate`
5. Install requirements : `pip install -r requirements.txt`
6. Move to `src`directory : `cd src/`
7. Execute the following command : `python main.py`

## Code organisation

 * **audios/** : Audio files.
 * **sprites/** : Contains multiple folders containing the image files.
 * **tileset/** : Background files.
 * **video/** : Video files.
 * **Boss.py** : Class dedicated to the Boss enemy, inherited from Supporters.
 * **Bullets.py** : Class representing a weapon's bullet.
 * **Capitol.py** : Class dedicated to the Capitol.
 * **Coequipier.py** : Class dedicated to the Coequipier (auto shoot from the Capitol).
 * **CONST.py** : Class containing all the constants.
 * **Gui.py** : Class dedicated to display the different buttons, texts and images over the game screen.
 * **main.py** : Main file used to run the entire project.
 * **Manager.py** : Class dedicated to the handling of the other classes.
 * **Player.py** : Class dedicated to the Player entity of the game.
 * **ProTrump.py** : Class dedicated to the ProTrump enemy, inherited from Supporters.
 * **Redneck.py** : Class dedicated to the Redneck enemy, inherited from Supporters.
 * **Strike.py** : Class associated to the button "*Do Not Click*".
 * **Supporter.py** : Parent class for the 3 different types of suppporters.
 * **Tweet.py** : Class dedicated to the pop-up event of Donald tweeting "*Stop the count!*".
 * **Weapon.py** : Class representing the Player weapon.

## Dependencies

 * Game Engines
    - [**Arcade**](https://arcade.academy/)
    - [**Pygame**](https://www.pygame.org/news)
 * Sprites from [**Superpowers Asset Packs**](https://github.com/sparklinlabs/superpowers-asset-packs)
 * Librairies
    - [**moviepy**](https://github.com/Zulko/moviepy)

## Authors

 * ARYS Louis
 * ARYS Simon
 * COUPLET Adrien
 * FISET Alexandre
