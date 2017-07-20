using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace MegaChallengeWar
{
    public partial class Default : System.Web.UI.Page
    {
        /*=============================================================
         * 
         *  Program MegaChallengeWar
         *  Author: Russell Stauffer
         *  Version: 1.0
         *  Date: 19 JUL 2017
         *  
         *  Based on an idea by Bob Tabor, Developer University.
         *  
         *  Compiler: C# (Visual Studio - 2017 Community Version)
         * 
         *  Description: This is a simulation of the card game of War.
         *  You create a deck, of type Card. You also have two players,
         *  and perform a game. This game can have multi-layered wars,
         *  and you can have ties. Since War can be nearly infinite in 
         *  length, I will limit it to 20 rounds. The game will also 
         *  end if one player runs out of cards.
         *  
         *  Note that in War, you normally do not get to see the 
         *  bounty, the hidden cards given when a War happens. In this
         *  version, the cards are hidden, but can be visualized by
         *  adding a StringBuilder to the game.cs Class via the
         *  gotWar function in the triple loop. 
         *  
         *  Bob Tabor's version grabbed the second of the three 
         *  cards in the war bounty drop, which is not required in 
         *  most versions of War. I used the traditional method of 
         *  two hidden cards, followed by the "Battle" card. Bob's
         *  method can be achieved using a "sandwich extract" in
         *  the gotWar method mentioned above, but was not a 
         *  requirement in the guidelines, and so was left out.
         *  
         * ============================================================
         */


        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void playButton_Click(object sender, EventArgs e)
        {
            Game game = new Game("Player1","Player2");
            resultLabel.Text = game.Play();
                       
        }
    }
}