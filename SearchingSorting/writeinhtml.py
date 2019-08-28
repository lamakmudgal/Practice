

voipandalitdrs = []
voipandalitdrs.append("""<html><head><style>
table, th, td {
    border: 1px solid black;
}
</style></head>
<body><p>Call Data Viewer Report</p><table style="width:100%"><tr>
    <th>Transaction ID</th>
    <th>Call Start Time</th>
    <th>Call End Time</th>
    <th>Call Duration</th>
    <th>Dailed Digits</th>
    <th>Calling Party Number</th>
    <th>Call Type</th>
    <th>Point Code</th>
    <th>Default Zone</th>
    <th>MSC ID</th>
    <th>ESRK/ESQK</th>
    <th>Sector Signaling ID</th>
    <th>CellSite Identifier</th>
    <th>Cell Site/eNodeB Address</th>
    <th>Cell Site/eNodeB Zip Code</th>
    <th>Cell Site/eNodeB City</th>
    <th>PSAP Group ID</th>
    <th>FCC PSAP ID</th>
    <th>FCC PSAP Name</th>
    <th>PSAP State</th>
    <th>PSAP County</th>
    <th>Deployed Phase of the PSAP</th>
    <th>ESN</th>
    <th>Trunk Select Codes</th>
    <th>Ali Bid Details</th>
    <th>Position data sent to PSAP</th>
    <th>UBP</th>
    <th>Dispatchable Location</th>
    <th>Additional Position Data Available<th>
  </tr>""")


voipandalitdrs.append("""</table></body></html>""")


with open("C:\\WorkStuff\\Python\\CDV_TDR_Mapper\\report.html",
          'w') as fpvoidtdr:
    for item in voipandalitdrs:
        fpvoidtdr.write("%s\n" % str(item))