using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

/* ====================================================================
 *  Program: Postal Cost Calculator
 *  Version: 1.0
 *  Primary Developer: Russell Stauffer
 *  Date: 19 June 2017
 *  
 *  Development Environment: C# language using Visual Studio 2015
 *  
 *  Description: This exercise is to determine the approximate or
 *  actual cost of shipment of a package based on the volume which the
 *  package will take. Note that weight is not used (a real-world 
 *  requirement for shipping costs.) This is an exercise in using 
 *  methods where incomplete information might be available, but an
 *  estimate of the cost is necessary.
 *  
 * ===================================================================*/


namespace ChallengePostalCalculatorHelperMethods
{
    public partial class PostalChallenge : System.Web.UI.Page
    {

        protected void Page_Load(object sender, EventArgs e)
        {

        }   
         
        protected void mainRoutine(object sender, EventArgs e)
        {
            // check for existance of textbox text and checked boxes

            if (!valuesExist()) return;

            // get dimensions and volume

            double outVolume = 0;
            if (!tryGetDimensions(out outVolume)) return;

            // get postal rate

            double postalRate = 0;
            getPostalRate(out postalRate);

            // Determine cost

            double packageCost = postalRate * outVolume;

            // Display to user
            // string outPackageCost = packageCost.ToString();
            resultText.Text = string.Format("This package will cost {0:C} to ship.", packageCost);
           
        }

        private bool valuesExist()
        {
            // Look for a check in the radio buttons.
            // airButton = air freight, groundButton is ground freight, 
            // nextDayButton = next day expedited freight

            if (!airButton.Checked && !groundButton.Checked && !nextDayButton.Checked)
                return false;

            // Look for values in text fields.
            // Cut out all whitespace, then look for length.
            // If zero, no values were entered.

            if (widthText.Text.Trim().Length == 0
                || heightText.Text.Trim().Length == 0)
                return false;

            return true;

        }

        private bool tryGetDimensions(out double outVolume)
        {
            // try to get the values for the dimensions.

            double newLength = 0;
            double newWidth = 0;
            double newHeight = 0;
            outVolume = 0;

            // check for usable values for height, width and length.

            if (!double.TryParse(widthText.Text.Trim(), out newWidth)) return false;
            if (!double.TryParse(heightText.Text.Trim(), out newHeight)) return false;
            if (!double.TryParse(lengthText.Text.Trim(), out newLength)) newLength = 1;

            // Calculate the volume (dimensions);

            outVolume = newLength * newWidth * newHeight;
            return true;
        }
       
        private void getPostalRate(out double postalRate)
        {
            postalRate = 0.0;  // set value

            if (groundButton.Checked) postalRate = 0.15;
            else if (airButton.Checked) postalRate = 0.25;
            else if (nextDayButton.Checked) postalRate = 0.45;
            else postalRate = 0.0;
        }
    }
}