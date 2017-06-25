$('.start-refresh.trigger').popover({
    html: true,
    title: 'Get value',
    content: function () {
        return $(this).parent().find('.content').html();
    }
});

$(document).on("click", "#popoverSubmit", function () {
    var inputval = $(".popover #popoverInput").val();
    $('.popover-markup').popover('hide');
    if (inputval === parseInt(inputval, 10)){
      document.getElementsByID('popoverInput')[0].placeholder=inputval+'min';
    return true;
  }
});

//label top page
if ('{{ tablename }}') {
  $('#heading').html('{{ tablename }}'+'  '+ '<span class="label label-pill label-warning" id="toplabel">Stopped</span>');
  $(".dropdown-toggle").val('{{ tablename }}');
};

//block save button in info textarea
$(document).ready(function() {
$('input[type="submit"]').attr('disabled', true);
$('input[type="text"],textarea').on('keyup',function() {
    var textarea_value = $("#text").val();
    var text_value = $('input[name="textField"]').val();
    if(textarea_value != '' && text_value != '') {
        $('input[type="submit"]').attr('disabled' , false);
    }else{
        $('input[type="submit"]').attr('disabled' , true);
    }
});
});

  var runState; // para identificar se a corrida está on a partir do python. Apagar abaixo se nao se usar esta var.

  $(function(){
    $('#runButton').click(function() {
      if ((this).text==="Stop" || runState) {
        (this).text = "Start"; runState=false; $ ('#toplabel').text("Stopped"); $ ("#runButton").removeClass("btn-warning btn-danger").addClass("btn-success");
      } else {(this).text="Stop"; runState=true; $ ('#toplabel').text("Running"); $ ("#runButton").removeClass("btn-warning btn-success").addClass("btn-danger active");}
    })
  });

  //datePeriod
  $(function() {
    $('input[name="daterange"]').daterangepicker();
  });

  $(function () {
      Highcharts.chart('temperature_plot', {
          xAxis: {
              categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
          },
          yAxis: {
              title: {
                  text: 'Temperature (°C)'
              },
              plotLines: [{
                  value: 0,
                  width: 1,
                  color: '#808080'
              }]
          },
          title:{
              text:''
          },
          legend:{
              enabled: false
          },
          tooltip: {
              valueSuffix: '°C'
          },
          series: [{
              name: 'T1',
              data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
          }, {
              name: 'T2',
              data: [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]
          }, {
              name: 'Troom',
              data: [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0]
          }]
      });
  });

  //
  //     google.load('visualization', '1', {packages: ['corechart']});
  //     google.setOnLoadCallback(drawChart);
  //     function drawChart() {
  //       var data = new google.visualization.DataTable();
  //       data.addColumn('datetime', 'Data');
  //       data.addColumn('number', 'T1');
  //       data.addColumn('number', 'T2');
  //       data.addColumn('number', 'Texterior');
  //       data.addRows([
  //        {% for row in records %}
  //        [new Date({{row[0][0:4]}},{{row[0][5:7]}},{{row[0][8:10]}},{{row[0][11:13]}},{{row[0][14:16]}}),
  //        {{'%0.2f'|format(row[1])}},
  //        {{'%0.2f'|format(row[2])}},
  //        {{'%0.2f'|format(row[3])}}],
  //        {% endfor %}
  //        ]);
  //
  //       var options = {
  //         width: 600,
  //         height: 563,
  //         hAxis: {
  //           title: "Data",
  //           gridlines: { count: {{records_items}}, color: '#CCC' },
  //           format: {'dd-MMM-yyyy HH:mm' },
  //           vAxis: {
  //              title: 'ºC'
  //           },
  //           title: 'Temperatura',
  //         curveType: 'function'  //Makes line curved
  //      };
  //      var chart = new google.visualization.LineChart(document.getElementById('chart_temps'));
  //      chart.draw(data, options);
  //   };
