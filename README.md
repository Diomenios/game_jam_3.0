# Redneck Ramble 

By Team : **C'était mieux avant**

## Code organisation

 * **sprites :** Contains all the sprites for the different games entities.
 * **main.py :** Is needed in order to make the game runnable. It's the first class excecuted by Python Arcade. 
 * **CONST.py :** Contains all the constants needed to set-up the game.
 * **Manager.py :** Class dedicated to the gestion of all the game event. For each trigger event, pass the event value to the right other game class.
 * **Player.py :** Class dedicated to the gestion of the Player entity. Contains all the methods for the gestion of the player mechanic and modify his properties
 * **Supporter.py :** Class dedicated to the gestion of the Supporter (generic ennemies) entity. Contains all the methods and attributes common to all the ennemies of the game.
 * **Weapon.py :** Class dedicated to the gestion of the Weapon entity. Contaisn all the attributes and methods needed in order to define the shape, number and dammage of the Bullet entities poped on player attack.

 Authors :  ARYS Louis, ARYS Simon, FISET Alexandre, COUPLET Adrien.