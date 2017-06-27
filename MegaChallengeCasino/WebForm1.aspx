<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="MegaChallengeCasino.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
    </div>
        <asp:Image ID="Reel1" runat="server" Height="150px" Width="150px" />
        <asp:Image ID="Reel2" runat="server" Height="150px" Width="150px" />
        <asp:Image ID="Reel3" runat="server" Height="150px" Width="150px" />
        <br />
        <br />
        Your Bet:&nbsp;
        <asp:TextBox ID="betTextBox" runat="server" Font-Size="Medium"></asp:TextBox>
        <br />
        <br />
        <asp:Button ID="spinButton" runat="server" OnClick="Button1_Click" Text="Pull The Lever!" />
        <br />
        <br />
        <asp:Label ID="outcomeLabel" runat="server"></asp:Label>
        <br />
        <br />
        Players Money $: <asp:Label ID="playersMoneyText" runat="server"></asp:Label>
        <br />
        <br />
        1 Cherry - x2 Your Bet<br />
        2 Cherries - x3 Your Bet<br />
        3 Cherries - x4 Your Bet<br />
        <br />
        3 7s - Jackpot - x100 Your Bet<br />
        <br />
        HOWEVER<br />
        <br />
        If there&#39;s even one BAR you win nothing.</form>
</body>
</html>
