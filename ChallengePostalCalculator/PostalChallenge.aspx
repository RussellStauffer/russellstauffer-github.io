<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="PostalChallenge.aspx.cs" Inherits="ChallengePostalCalculatorHelperMethods.PostalChallenge" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        <h3>Postal Calculator</h3>
        <p>
            &nbsp;</p>
        <p>
            Width:
            <asp:TextBox ID="widthText" runat="server" OnTextChanged="mainRoutine"></asp:TextBox>
        </p>
        <p>
            Height:
            <asp:TextBox ID="heightText" runat="server" AutoPostBack="True" OnTextChanged="mainRoutine"></asp:TextBox>
        </p>
        <p>
            Length:
            <asp:TextBox ID="lengthText" runat="server" AutoPostBack="True" OnTextChanged="mainRoutine"></asp:TextBox>
        </p>
        <p>
            &nbsp;</p>
        <p>
            <asp:RadioButton ID="groundButton" runat="server" AutoPostBack="True" GroupName="rateButton" Text="Ground" OnCheckedChanged="mainRoutine" />
        </p>
        <p>
            <asp:RadioButton ID="airButton" runat="server" AutoPostBack="True" GroupName="rateButton" Text="Air" OnCheckedChanged="mainRoutine" />
        </p>
        <p>
            <asp:RadioButton ID="nextDayButton" runat="server" AutoPostBack="True" GroupName="rateButton" Text="Next Day" OnCheckedChanged="mainRoutine" />
        </p>
        <p>
            <asp:Label ID="resultText" runat="server"></asp:Label>
        </p>
        <p>
            &nbsp;</p>
    
    </div>
    </form>
</body>
</html>
