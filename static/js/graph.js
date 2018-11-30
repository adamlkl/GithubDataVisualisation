queue()
    .defer(d3.json, '/bloombergdata/repo_data2')
    .await(makeGraphs);

function makeGraphs(error, projectsJson){
    var bloomberg_repo = projectsJson;
    var ndx = crossfilter(bloomberg_repo);
    var repoName = ndx.dimension(function (d) {return d.Name;});
    var repoSize = ndx.dimension(function (d) {return d.Size;});
    var lang = ndx.dimension(function (d) {return d.Languages;},true);
    var langGroup = lang.group()

    var repoLOC = ndx.dimension(function (d) {
        return d.TotalLOC;
    });


    var all = ndx.groupAll();
    var rnamebySize = repoName.group().reduceSum();
    var LOCbyName = repoLOC.group();
    var sizebyName = repoSize.group();
    var pie1 = dc.pieChart('#pie')
        .width(500)
        .height(500)
        .innerRadius(25)
        .label(function(d) {
                    return d.key + ': ' + d.value;
            })
        .dimension(dimensionCategory)
        .group(quantityByCategory);


};