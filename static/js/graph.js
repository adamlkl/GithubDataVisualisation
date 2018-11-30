queue()
    .defer(d3.json, "/bloombergdata/repo_data")
    .await(makeGraphs);

