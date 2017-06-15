<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="EpicSpiesAssets.aspx.cs" Inherits="EpicSpiesAssetTracker.EpicSpiesAssets" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .auto-style2 {
            font-size: medium;
        }
        .auto-style3 {
            font-size: medium;
            font-weight: normal;
        }
        .auto-style4 {
            font-weight: normal;
        }
        .newStyle1 {
            font-family: Arial, Helvetica, sans-serif;
            font-size: x-large;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
    <div style="font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; font-size: medium; font-weight: normal">
    
        <h3>
            <asp:Image ID="Image1" runat="server" Height="150px" ImageUrl="~/epic-spies-logo.jpg" />
            <br />
            <br />
            <span class="newStyle1"><strong>Asset Performance Tracker</strong></span></h3>
        <h3><span class="auto-style3">Asset Name: </span>
            <asp:TextBox ID="assetNameText" runat="server"></asp:TextBox>
            <span class="auto-style4">
            <br class="auto-style2" />
            <br class="auto-style2" />
            </span><span class="auto-style3">Elections Rigged: </span>
            <asp:TextBox ID="electionsCountText" runat="server"></asp:TextBox>
            <span class="auto-style4">
            <br class="auto-style2" />
            <br class="auto-style2" />
            </span><span class="auto-style3">Acts of Subterfuge Performed: </span>
            <asp:TextBox ID="subterfugeCountText" runat="server"></asp:TextBox>
        </h3>
        <p>
            <asp:Button ID="assetButton" runat="server" OnClick="assetButton_Click" Text="Add Asset" />
        </p>
    
    </div>
        <asp:Label ID="resultLabel" runat="server"></asp:Label>
    </form>
</body>
</html>
