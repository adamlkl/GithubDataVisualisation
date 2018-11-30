queue()
    .defer(d3.json, 'repo_data2.json')
    .await(makeGraphs);

function makeGraphs(error, projectsJson){
    var bloomberg_repo = projectsJson;
    var ndx = crossfilter(bloomberg_repo);
    var repoName = ndx.dimension(function (d) {
        return d.Name;
    });
    var repoSize = ndx.dimension(function (d) {
        return d.Size;
    });
    var lang = ndx.dimension(function (d) {
        return d.Languages;
    });
    var repoLOC = ndx.dimension(function (d) {
        return d.TotalLOC;
    });


    var all = ndx.groupAll();
    var rname = repoName.group();
    var LOCbyName = repoLOC.group();
    var sizebyName = repoSize.group();
    var chart = dc.bubbleChart('#bubble')

};