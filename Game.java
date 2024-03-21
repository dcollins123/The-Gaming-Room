package com.gamingroom;


/**
 * A simple class to hold information about a game
 * 
 * <p>
 * Notice the overloaded constructor that requires
 * an id and name to be passed when creating.
 * Also note that no mutators (setters) defined so
 * these values cannot be changed once a game is
 * created.
 * </p>
 * 
 * @Daniel Collins daniel.collins6@snhu.edu
 *
 */
public class Game extends Entity {
	
	public Game(long id, String name) {  // Constructor with an identifier and name
		super(id, name);
	}

}
