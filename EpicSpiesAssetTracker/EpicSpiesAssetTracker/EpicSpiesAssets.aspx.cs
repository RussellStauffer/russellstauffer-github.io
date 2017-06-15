using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace EpicSpiesAssetTracker
{
    public partial class EpicSpiesAssets : System.Web.UI.Page
    {

        protected void Page_Load(object sender, EventArgs e)
        {
            if (!Page.IsPostBack)
            {
                // Initialize arrays for spy, elections and subterfuge
                // remember to begin at zero.

                string[] spyArray = new string[0];
                int[] electionArray = new int[0];
                int[] subterfugeArray = new int[0];

                ViewState.Add("Assets", spyArray);
                ViewState.Add("Elections", electionArray);
                ViewState.Add("Acts", subterfugeArray);
            }
        }

        protected void assetButton_Click(object sender, EventArgs e)
        {
            // Get data from ViewState

            string [] spyArray = (string[]) ViewState["Assets"];
            int [] electionArray = (int[]) ViewState["Elections"];
            int[] subterfugeArray = (int[]) ViewState["Acts"];

            // Get the new length for the expanding strings

            int newLength = spyArray.Length + 1;

            // resize the arrays

            Array.Resize(ref spyArray, newLength);
            Array.Resize(ref electionArray, newLength);
            Array.Resize(ref subterfugeArray, newLength);

            // Bring the data from the text fields

            string assetName = assetNameText.Text;
            int electionsRigged = int.Parse(electionsCountText.Text);
            int actsSubterfuge = int.Parse(subterfugeCountText.Text);

            int hiIndex = spyArray.GetUpperBound(0);

            spyArray[hiIndex] = assetName;
            electionArray[hiIndex] = electionsRigged;
            subterfugeArray[hiIndex] = actsSubterfuge;

            ViewState["Assets"] = spyArray;
            ViewState["Elections"] = electionArray;
            ViewState["Acts"] = subterfugeArray;

            // Print Statistics (Total Elections Rigged, Average acts 
            // of subterfuge, and last asset you added.

            // --- calculate total elections rigged ---

            int totElections = electionArray.Sum();

            // --- get the average acts of subterfuge

            double avgSubterfuge = subterfugeArray.Average();

            //resultLabel.Text = "<br /> Average acts of subterfuge: {1}" + avgSubterfuge.ToString();

            resultLabel.Text = String.Format("Total Elections Rigged: {0} <br /> Average acts of subterfuge: {1} <br /> Last Asset Added: {2}",
                totElections.ToString(),
                avgSubterfuge.ToString(),
                spyArray[hiIndex]);

            // clear text fields after output

            assetNameText.Text = "";
            electionsCountText.Text = "";
            subterfugeCountText.Text = "";

        }
    }
}