function hideAllCollapsibles() {
    $('.panel-collapse.collapse.in').each(function(index) {
        $(this).collapse('hide');
    });
}

function changeTab(tabtype) {
    var selected_tab = '#myTab a[href="#' + tabtype + '"]';
    $(selected_tab).tab('show') ; // Select tab by name

}

function selectCollapsible(collapse, position) {
    var selected_collapse = '#' + collapse;
    var selected_position = '#' + position;
    console.log($(selected_position).offset());
    $(selected_collapse).collapse('show'); //show collapsible item
    $(selected_position).ScrollTo(); // scroll to item
    //$('html, body').animate({scrollTop: $(position).offset().top}, 500);
    //$('html, body').animate({scrollTop: $(selected_collapse).offset().top}, 1000);
}

function linkToPaper(tabtype, collapse, position) {
    hideAllCollapsibles();
    changeTab(tabtype);
    var delay = 700; //1 seconds
    setTimeout(function() {
        selectCollapsible(collapse, position);
    }, delay);
}
