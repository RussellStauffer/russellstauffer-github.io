using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace ChallengePhunWithStrings
{
    public partial class Default : System.Web.UI.Page
    {
        /*=============================================================
         * 
         *      Challenge "Phun" with Strings
         * 
         *      Compiled on: Visual Studio 2015
         *      Programming Language: C#
         *      Version 1.1
         *      
         *      Author: Russell Stauffer
         *      Date: 28 June 2017
         *      
         *      Original Concept by Bob Tabor, Developer University
         * 
         ============================================================*/
        protected void Page_Load(object sender, EventArgs e)
        {
            // 1.  Reverse your name
            // In my case, the result would be:
            // robaT boB

            // Developer notes: Separate the string into an array of
            // characters, then reverse the characters using the
            // array reverse.

            string name = "Bob Tabor";
            char[] textArray = name.ToCharArray();
            Array.Reverse(textArray);
            resultLabel.Text = new string (textArray);

//---------------------------------------------------------------------

            // 2.  Reverse this sequence:
            string names = "Luke,Leia,Han,Chewbacca";
            // When you're finished it should look like this:
            // Chewbacca,Han,Leia,Luke

            // Developers Notes: Split this string into four
            // elements, then re-merge.

            string[] newOrder = names.Split(',');
            Array.Reverse(newOrder);
            string newNamesList = string.Join(",", newOrder);

            result2Label.Text = newNamesList;

            //---------------------------------------------------------------------


            // 3. Use the sequence to create ascii art:
            // *****luke*****
            // *****leia*****
            // *****han******
            // **Chewbacca***

            // developer notes:
            // First, reverse newOrder to create the original string.
            Array.Reverse(newOrder);

            // Second, determine the length of the string, 
            // then the padding on the left, then the padding on the
            // right. 
            string artString = "";

            for (int i = 0; i < newOrder.Length; i++)
            {
                int j = (14 - (newOrder[i].Length)) / 2;
                string temp = newOrder[i].PadRight(14 - j,'*');
                artString += temp.PadLeft(14, '*');
                artString += "<br />";               
            }
            result3Label.Text = artString;

            //---------------------------------------------------------------------

            // 4. Solve this puzzle:

            string puzzle = "NOW IS ZHEremove-me ZIME FOR ALL GOOD MEN ZO COME ZO ZHE AID OF ZHEIR COUNZRY.";



            // Once you fix it with string helper methods, it should read:
            // Now is the time for all good men to come to the aid of their country.

            // Developer notes: You need to 
            // 1) turn all Zs to Ts
            String temp2 = puzzle.Replace("Z", "T");


            // 2) remove the term "remove-me"
            int value = temp2.IndexOf("remove-me");
            puzzle = temp2.Remove(value, value + 8);

            // 3) Remove all caps except the first.

            temp2 = puzzle.ToLower(); // convert all uppercase to lower.

            // convert the first character to upper, and reattach to
            // the rest of the sentence string.

            temp2 = temp2.First().ToString().ToUpper() + temp2.Substring(1);
            
            // Note: This is actually better than Bob Tabor's original 
            // solution, as it works for any sentence string.

            result4Label.Text = temp2;
        }
    }
}