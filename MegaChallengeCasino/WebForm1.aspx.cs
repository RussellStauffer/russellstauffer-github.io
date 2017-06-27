using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace MegaChallengeCasino
{

    // ================================================================
    //  Megachallenge Casino Slot Machine Exercise
    //  
    //  Version 1.1 (student modifications)
    //
    //  Software Developer: Russell Stauffer
    //  Created on: 23-27 JUN 2017
    //
    //  Compiler: C# Visual Studio 2015 (also works on V/S 2017)
    //
    //  Original Concept by Developers Unversity
    //
    //=================================================================
/*=====================================================================  
 *  Description: This exercise in C# / ASP.NET is to create a program 
 *  with the smallest code modules as possible. No module is over 6 
 *  lines in length (comments not included.) 
 * ====================================================================*/

    public partial class WebForm1 : System.Web.UI.Page
    {
        // create the random number (randNum) generator.

        Random randNum = new Random(); // randomizer for reels

        protected void Page_Load(object sender, EventArgs e)
        {
            if (!Page.IsPostBack) // Initializations
            {
                // initialize reel display
                string[] reels = reelSpin();
                showReels(reels);
                // Set player money
                ViewState.Add("PlayersMoney", 100);
                displayPlayersMoney();
            }
        }

        protected void Button1_Click(object sender, EventArgs e)

        {
            // Check to see if the bet is numeric. If yes, pull the
            // handle, and display the outcome (win or lose) and
            // then update the players available balance.

            int playersBet;

            if (!int.TryParse(betTextBox.Text, out playersBet)) return;
            
            int playersWin = handlePull(playersBet);             //

            if (playersWin > 0) youWin(playersWin, playersBet);
            else youLose(playersBet);
             
            displayPlayersMoney();  // display outcome
        }

        /*=====================================================================
         *  Display Section
         */
        //===================================================================


        private string[] reelSpin ()
        {
            // return a new set of three reel images

            string[] reelImage = new string[] { setImages(), setImages(), setImages() };
            return reelImage;
        }
        
        private void showReels(string[] reelImage)
        {
            // pass new images to the reel display.

            Reel1.ImageUrl = "/Images/" + reelImage[0] + ".png";
            Reel2.ImageUrl = "/Images/" + reelImage[1] + ".png";
            Reel3.ImageUrl = "/Images/" + reelImage[2] + ".png";
        }
      
        private string setImages()
        { 
            // Set the available image types to images.

            string[] images = new string[] { "Bar", "Bell", "Cherry", "Clover",
            "Diamond","Horseshoe","Lemon","Orange","Plum","Seven",
            "Strawberry","Watermelon" };
        
            return images[randNum.Next(11)];
        }

        /*=============================================================
         * First Spin
         ============================================================*/ 

       private int handlePull(int playersBet)
        {
            string[] reelImage = reelSpin(); 
            showReels(reelImage);
            // outcomeLabel.Text = String.Format("{0},{1},{2}", reelImage[0], reelImage[1], reelImage[2]);
            int multiplier = evaluateReels(reelImage);
            int playersWin  = multiplier * playersBet;
            return playersWin; 
        } 
            
        /*=====================================================================
        *  Outcome Evaluation Section (Payout)
        * ====================================================================
        */
        private void displayPlayersMoney()
        { 
            // this section displays players money from the ViewState.
            playersMoneyText.Text = ViewState["PlayersMoney"].ToString();
        }

        private int payOut(string[] reelImage, int playersBet)
        {
            // This section determines the winnings

            int mult = evaluateReels(reelImage);
            int playersWin = playersBet * mult ;
            return playersWin; 
        }

        //
        // === Reel Evaluations ===============================================
        //
        private int evaluateReels(string[] reelImage)
        {
            // This section determines the multiplier for winnings.

            int mult = gotCherries(reelImage);
            if (gotSevens(reelImage)) mult = 100;
            if (gotBars(reelImage)) mult = 0;
            return mult;
        }

        private int gotCherries(string[] reelImage)
        {
            // this section determines the multiplier if the
            // spin has cherries in it.

            int multiplier = 0;

            if (reelImage[0] == "Cherry") multiplier++;
            if (reelImage[1] == "Cherry") multiplier++;
            if (reelImage[2] == "Cherry") multiplier++;

            if (multiplier > 0) multiplier++;

            return multiplier;
        }

        private bool gotSevens(string[] reelImage)
        { 
            // If we have three sevens, we will use a x100 multiplier
            // in function EvaluateReels

            if (reelImage[0] == "Seven" && reelImage[1] == "Seven" &&
                reelImage[2] == "Seven") return true;

            return false;
        }

        private bool gotBars(string[] reelImage)
        {
            // if any bars show in the payout line, the multiplier
            // goes to zero in EvaluateReels.

            if (reelImage[0] == "Bar" || reelImage[1] == "Bar"
                  || reelImage[2] == "Bar") return true;

            return false;
        }
 
        private bool didYouWin(string[] reelImage, int playersBet)
        {
            // check to see if you won or lost. Lose condition
            // is if winnings (gotWin) equal zero.

            int gotWin = payOut(reelImage, playersBet);
            if (gotWin == 0) return false;
            else return true;
        }
       

        // ===== outcome results ===================================

        private void youWin(int playersWin, int playersBet)
        {
            // Winning conditions, update players money and display.
            // Add winnings, subtract bet. 

            int playersMoney = int.Parse(ViewState["PlayersMoney"].ToString());
            playersMoney = (playersMoney + playersWin - playersBet);
            ViewState["PlayersMoney"] = playersMoney;
            outcomeLabel.Text = String.Format("You bet {0:C} and won {1:C}. Congratulations!", playersBet, playersWin);
        }

        private void youLose(int playersBet)
        { 
            // Losing conditions. Subtract bet from players money.

            int playersMoney = int.Parse(ViewState["PlayersMoney"].ToString());
            outcomeLabel.Text = string.Format("You did not win. You lose {0:C}", playersBet);
            playersMoney = playersMoney - playersBet;
            ViewState["PlayersMoney"] = playersMoney;
        }
/*===========================================================================
 *  End of Program.
 *  
 *  Notes: There are several flaws in this program, the most notable being
 *  that there is no break when the player is out of money. However, that
 *  was not part of the specification, but could be included in a later
 *  version of the program. The six-line method may need to be modified
 *  to allow for further modifications in a timely fashion.
 *=========================================================================*/ 
    }
} 