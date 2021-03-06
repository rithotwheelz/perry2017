    var oldStatus = 2;
    var newStatus = 1;

    $(document).ready(function () {
          $('#speed').jqxGauge({
              ranges: [{ startValue: 0, endValue: 40, style: { fill: '#4cb848', stroke: '#4cb848' }, startDistance: 0, endDistance: 0, endWidth: 13, startWidth: 13},
                  { startValue: 40, endValue: 60, style: { fill: '#fad00b', stroke: '#fad00b' }, startDistance: 0, endDistance: 0, endWidth: 13, startWidth: 13},
                  { startValue: 60, endValue: 80, style: { fill: '#e53d37', stroke: '#e53d37' }, startDistance: 0, endDistance: 0, endWidth: 13, startWidth: 13}],
                cap: { size: '5%', style: { fill: '#2e79bb', stroke: '#2e79bb'} },
                border: { style: { fill: '#f957d9', stroke: '#7b8384', 'stroke-width': 1 } },
                ticksMinor: { interval: 2.5, size: '5%' },
                ticksMajor: { interval: 10, size: '10%' },       
                labels: { position: 'outside', interval: 10 },
                pointer: { style: { fill: '#2e79bb' }, width: 5 },
                animationDuration: 500,
                caption: { offset: [0, -25], value: 'MPH', position: 'bottom' },
                min: 0,
                max: 80,
                style: { fill: '#b2adb1', stroke: '#d608ad' },
                height: 275,
                value: 0
          });

          $('#speed').on('valueChanging', function (e) {
                $('#speedVal').text(Math.round(e.args.value) + ' mph');
            });

          $('#RPM').jqxGauge({
              ranges: [{ startValue: 0, endValue: 5, style: { fill: '#4cb848', stroke: '#4cb848' }, startDistance: 0, endDistance: 0, endWidth: 13, startWidth: 13},
                { startValue: 5, endValue: 7, style: { fill: '#fad00b', stroke: '#fad00b' }, startDistance: 0, endDistance: 0, endWidth: 13, startWidth: 13},
                { startValue: 7, endValue: 8, style: { fill: '#e53d37', stroke: '#e53d37' }, startDistance: 0, endDistance: 0, endWidth: 13, startWidth: 13}],
                cap: { size: '5%', style: { fill: '#2e79bb', stroke: '#2e79bb'} },
                border: { style: { fill: '#f957d9', stroke: '#7b8384', 'stroke-width': 0.5 } },
                ticksMinor: { interval: 0.25, size: '5%' },
                ticksMajor: { interval: 1, size: '10%' },       
                labels: { position: 'outside', interval: 1 },
                pointer: { style: { fill: '#2e79bb' }, width: 5 },
                animationDuration: 500,
                caption: { offset: [0, -25], value: 'RPM', position: 'bottom' },
                min: 0,
                max: 8,
                style: { fill: '#b2adb1', stroke: '#d608ad' },
                height: 275, 
                value: 0
          });

          $('#RPM').on('valueChanging', function (e) {
                $('#RPMVal').text(Math.round(e.args.value) + ' rpm');
            });

          $('#accel').jqxGauge({
              ranges: [{ startValue: 0, endValue: 5, style: { fill: '#4cb848', stroke: '#4cb848' }, startDistance: 0, endDistance: 0, endWidth: 13, startWidth: 13},
                { startValue: 5, endValue: 7, style: { fill: '#fad00b', stroke: '#fad00b' }, startDistance: 0, endDistance: 0, endWidth: 13, startWidth: 13},
                { startValue: 7, endValue: 8, style: { fill: '#e53d37', stroke: '#e53d37' }, startDistance: 0, endDistance: 0, endWidth: 13, startWidth: 13}],
                cap: { size: '5%', style: { fill: '#2e79bb', stroke: '#2e79bb'} },
                border: { style: { fill: '#f957d9', stroke: '#7b8384', 'stroke-width': 0.5 } },
                ticksMinor: { interval: 0.5, size: '5%' },
                ticksMajor: { interval: 2, size: '10%' },       
                labels: { position: 'outside', interval: 1 },
                pointer: { style: { fill: '#2e79bb' }, width: 5 },
                animationDuration: 500,
                caption: { offset: [0, -25], value: 'm/s2', position: 'bottom' },
                min: 0,
                max: 10,
                style: { fill: '#b2adb1', stroke: '#d608ad' },
                height: 200,
                value: 0
          });

          $('#accel').on('valueChanging', function (e) {
                $('#accelVal').text(Math.round(e.args.value) + ' g');
            });

          var majorTicks = { size: '10%', interval: 50 },
              minorTicks = { size: '5%', interval: 10, style: { 'stroke-width': 1, stroke: '#ffffff'} }

            $('#contCurr').jqxLinearGauge({
                orientation: 'vertical',
                ticksMajor: majorTicks,
                ticksMinor: minorTicks,
                ticksPosition: 'near',
                max: 500,
                min: 0,
                width: 200,
                value: 0,
                pointer: { size: '6%' },
                colorScheme: 'scheme03',
                background: { visible: false },
                labels: 	{ position: 'near', interval: 50, offset: 10}

            });

            $('#packCurr').jqxLinearGauge({
                orientation: 'vertical',
                ticksMajor: majorTicks,
                ticksMinor: minorTicks,
                ticksPosition: 'near',
                max: 500,
                min: 0,
                width: 200,
                value: 0,
                pointer: { size: '6%' },
                colorScheme: 'scheme02',
                background: { visible: false },
                labels: 	{ position: 'near', interval: 50, offset: 10}

            });

            $('#kwh').jqxLinearGauge({
                orientation: 'vertical',
                ticksMajor: majorTicks,
                ticksMinor: minorTicks,
                ticksPosition: 'near',
                max: 200,
                min: 0,
                width: 200,
                value: 0,
                pointer: { size: '6%' },
                colorScheme: 'scheme02',
                background: { visible: false },
                labels: 	{ position: 'near', interval: 20, offset: 10}

            });

            $('#soc').jqxLinearGauge({
                orientation: 'vertical',
                ticksMajor: { size: '10%', interval: 20 },
                ticksMinor: { size: '5%', interval: 5, style: { 'stroke-width': 1, stroke: '#ffffff'} },
                ticksPosition: 'near',
                max: 100,
                min: 0,
                width: 275,
                value: 0,
                pointer: { size: '6%' },
                colorScheme: 'scheme06',
                background: { visible: false },
                labels: 	{ position: 'near', interval: 20, offset: 10}

            });

            $('#capVolt').jqxLinearGauge({
                orientation: 'horizontal',
                ticksMajor: { size: '10%', interval: 20 },
                ticksMinor: { size: '5%', interval: 5, style: { 'stroke-width': 1, stroke: '#ffffff'} },
                ticksPosition: 'far',
                max: 165,
                min: 0,
                value: 0,
                pointer: { size: '6%' },
                colorScheme: 'scheme02',
                background: { visible: false },
                labels: 	{ position: 'far', interval: 20},
                height: 200,
                width: 300
            });

            $('#packVolt').jqxLinearGauge({
                orientation: 'horizontal',
                ticksMajor: { size: '10%', interval: 20 },
                ticksMinor: { size: '5%', interval: 5, style: { 'stroke-width': 1, stroke: '#ffffff'} },
                ticksPosition: 'far',
                max: 165,
                min: 0,
                value: 0,
                pointer: { size: '6%' },
                colorScheme: 'scheme02',
                background: { visible: false },
                labels: 	{ position: 'far', interval: 20},
                height: 200,
                width: 300
            });

            $('#ksi').jqxLinearGauge({
                orientation: 'horizontal',
                ticksMajor: { size: '10%', interval: 2 },
                ticksMinor: { size: '5%', interval: 0.5, style: { 'stroke-width': 1, stroke: '#ffffff'} },
                ticksPosition: 'far',
                max: 13,
                min: 0,
                value: 0,
                pointer: { size: '6%' },
                colorScheme: 'scheme02',
                background: { visible: false },
                labels: 	{ position: 'far', interval: 2},
                height: 200,
                width: 300
            });

            $('#bargauge').jqxBarGauge({
                colorScheme: "scheme01", 
                width: 400, 
                height: 400,
                values: [0, 0, 0, 0, 0], 
                max: 500, 
                tooltip: {visible: true, formatFunction: 
                  function (value, index)
                    {
                        var realVal = parseInt(value);
                        if (index == 0) {
                          return ("Low Battery Temperature: " + realVal + " °F");	
                        } else if (index == 1){
                          return ("Avg Battery Temperature: " + realVal + " °F");
                        } else if (index == 2){
                          return ("High Battery Temperature: " + realVal + " °F");
                        } else if (index == 3){
                          return ("Controller Temperature: " + realVal + " °F");
                        } else {
                          return ("Motor Temperature: " + realVal + " °F");
                        }
                    },
                }
            });

          $("#fault0").jqxExpander({ 
            width: '350px',
            expanded: false,
            disabled: true
          });

          $("#fault1").jqxExpander({ 
            width: '350px',
            expanded: false,
            disabled: true
          });

          $("#fault2").jqxExpander({ 
            width: '350px',
            expanded: false,
            disabled: true
          });

          $("#fault3").jqxExpander({ 
            width: '350px',
            expanded: false,
            disabled: true
          });

          $("#fault4").jqxExpander({ 
            width: '350px',
            expanded: false,
            disabled: true
          });

          $("#fault5").jqxExpander({ 
            width: '350px',
            expanded: false,
            disabled: true
          });

          $("#fault6").jqxExpander({ 
            width: '350px',
            expanded: false,
            disabled: true
          });  

          var data = [];
          // var max = 800;
          // var timestamp = new Date();
          // for (var i = 0; i < 30; i++) {
          //     timestamp.setMilliseconds(0);
          //     // timestamp.setSeconds(timestamp.getSeconds() - 1);
          //     timestamp.setSeconds(timestamp.getSeconds() - 1);
          //     timestamp.setMinutes(timestamp.getMinutes() - 1);
          //     data.push({ timestamp: new Date(timestamp.valueOf()), value: Math.max(100, (Math.random() * 1000) % max) });
          // }
          // data = data.reverse();      

          var settings = {
                title: "Kilowatt Hours usage",
                description: " ",
                enableAnimations: false,
                animationDuration: 1000,
                enableAxisTextAnimation: true,
                showLegend: false,
                padding: { left: 5, top: 5, right: 5, bottom: 5 },
                titlePadding: { left: 0, top: 0, right: 0, bottom: 10 },
                source: data,
                xAxis:
                {
                    dataField: 'timestamp',
                    type: 'date',
                    baseUnit: 'second',
                    unitInterval: 30,
                    formatFunction: function (value) {
                        return $.jqx.dataFormat.formatdate(value, "hh:mm:ss", 'en-us');
                    },
                    gridLines: { step: 7 },
                    valuesOnTicks: true,
                    labels: { angle: -45, offset: { x: -17, y: 0} }
                },
                colorScheme: 'scheme03',
                columnSeriesOverlap: 'true',
                seriesGroups:
                    [
                        {
                            type: 'splinearea',
                            columnsGapPercent: 100,
                            alignEndPointsWithIntervals: true,
                            valueAxis:
                            {
                                minValue: 0,
                                maxValue: 1000,
                                title: { text: 'Index Value' }
                            },
                            series: [
                                    { dataField: 'value', displayText: 'value', opacity: 1, lineWidth: 2, symbolType: 'circle', fillColorSymbolSelected: 'white', symbolSize: 4 }
                                ]
                        }
                    ]
            };
            // create the chart
            $('#chartContainer').jqxChart(settings);
            // auto update timer
          var ttimer = setInterval(function () {
              var max = 800;
              if (data.length >= 60)
                  data.splice(0, 1);
              var timestamp = new Date();
              timestamp.setSeconds(timestamp.getSeconds() - 1);
              timestamp.setMilliseconds(0);
              data.push({ timestamp: timestamp, value: Math.max(100, (Math.random() * 1000) % max) });
              $('#chartContainer').jqxChart('update');
          }, 2000);

    });

    $( document ).ready(function update_values(){
          $.getJSON("/_thing", function(data) {
            $('#capVolt').jqxLinearGauge('value', data.capVolt);
              $('#contCurr').jqxLinearGauge('value', data.contCurr);

              if (data.packCurr > 1000){
                $('#packCurr').jqxLinearGauge('value', 0);
              }else{
                $('#packCurr').jqxLinearGauge('value', data.packCurr);
              }
              $('#packVolt').jqxLinearGauge('value', data.packVolt);
              $('#soc').jqxLinearGauge('value', data.soc);
              $('#kwh').jqxLinearGauge('value', 50);
              $('#ksi').jqxLinearGauge('value', data.ksi);
            $('#speed').jqxGauge('value', data.speed);
            $('#RPM').jqxGauge('value', data.RPM);

            var kwNum = 0;
            $('#kwh').jqxLinearGauge('value', kwNum);

            $('#bargauge').jqxBarGauge('values', [data.lTemp, data.aTemp, data.hTemp, data.cTemp, data.motorTemp]);

            if (newStatus == oldStatus){
                  $("#status").text("System Offline..")
                  document.querySelector("#status").style.color = "red";
                }else{
                  $("#status").text("System Online..")
                  document.querySelector("#status").style.color = "green";
                }
                oldStatus = newStatus;

                // Need to clear all old faults first
                for (var j = 0; j < clength; j++) {
                  var num = j.toString();
                  $("#f".concat(num,"title")).text("...");
                  $("#fault".concat(num)).jqxExpander('disabled', true);
                };

                var clength = data.contFaults.length;

                if (clength > 0) {
                  for (var i = 0; i < clength; i++) {
                    if (data.contFaults[i] != 0){
                      var f = 0;
                      var header = $("#fault".concat(f.toString())).jqxExpander('getHeaderContent'); 

                      //make sure only empty ones are written to
                      while (header != "..."){
                        f++;

                        if (f > 7){
                          alert("FAULT OVERLOAD!!!")
                          console.log("Controller Faults: " + data.bmsFaults)
                        }

                        header = $("#fault".concat(f.toString())).jqxExpander('getHeaderContent'); 
                      }

                      var fstr = f.toString();
                      $("#fault".concat(fstr)).jqxExpander('disabled', false);

                      $("#f".concat(fstr, "title")).text(data.contFaults[i]);

                      switch(data.contFaults[i]){
                        case("Main Contactor Welded"):
                          $("#f".concat(fstr, "list")).append("Possible causes: <br><li>Main contactor tips are welded closed.</li> <li>Motor phase U or V is disconnected/open.</li> <li>An alternate voltage path (such as an external precharge resistor) is providing a current to the capacitor bank (B+ connection terminal).</li> <br> Recycle KSI to clear fault");
                          break;

                        case("Main Contactor Did Not Close"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Pot Low Overcurrent"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Throttle Wiper Low"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Throttle Wiper High"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Pot2 Wiper Low"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Pot2 Wiper High"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("EEPROM Failure"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("HPD/Sequencing Fault"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Severe B+ Undervoltage"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Severe B+ Overvoltage"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("B+ Undervoltage Cutback"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("B+ Overvoltage Cutback"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Not Used"):
                          $("#f".concat(fstr, "list")).append("Unknown Controller Fault.");
                          break;

                case("Controller Overtemp Cutback"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Controller Severe Undertemp"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Controller Severe Overtemp"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Coill Driver Open/Short"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Coil2 Driver Open/Short"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Coil3 Driver Open/Short"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Coil4 Driver Open/Short"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("PD Open/Short"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Main Open/Short"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("EMBrake Open/Short"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Precharge Failed"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Digital Out 6 Overcurrent"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Digital Out 7 Overcurrent"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Controller Overcurrent"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Current Sensor Fault"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Motor Temp Hot Cutback"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Parameter Change Fault"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Motor Open"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("External Supply Out of Range"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Motor Temp Sensor Fault"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("VCL Run Time Error"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("+5V Supply Failure"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("OS General"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("PDO Timeout"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Encoder Fault"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Stall Detected"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Motor Type Fault"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Supervisor Fault"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Motor Characterization Fault"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("VCL/OS Mismatch"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Encoder LOS (Limited Operating Strategy)"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Severe KSI Undervoltage"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Severe KSI Overvoltage"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Insulation Resistance Low"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;

                        case("Encoder Pulse Count Fault"):
                          $("#f".concat(fstr, "list")).append("Controller Fault");
                          break;


                        default:
                          $("#f".concat(fstr, "list")).append("No information available.");
                      }	
                    }
                  };
                }

                var blength = data.bmsFaults.length;

                if (blength > 0) {
                  for (var i = 0; i < blength; i++) {
                    if (data.bmsFaults[i] != 0){
                      var f = 0;
                      var header = $("#fault".concat(f.toString())).jqxExpander('getHeaderContent');

                      //make sure only empty ones are written to
                      while (header != "..."){
                        f++;

                        if (f > 7){
                          alert("FAULT OVERLOAD!!!")
                          console.log("BMS Faults: " + data.bmsFaults)
                        }

                        header = $("#fault".concat(f.toString())).jqxExpander('getHeaderContent'); 
                      }

                      var fstr = f.toString();
                      $("#fault".concat(fstr)).jqxExpander('disabled', false);

                      $("#f".concat(fstr, "title")).text(data.bmsFaults[i]);

                      switch(data.bmsFaults[i]){
                        case("Internal Communication"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("Internal Conversion"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("Weak Cell"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("Low Cell Voltage"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("Open Wiring"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("Current Sensor"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("Pack Voltage Sensor"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("Weak Pack"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("Voltage Redundancy"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("Fan Monitor"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("Thermistor"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("CANBUS Communication"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("Always-On Supply"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("High Voltage Isolation"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("12V Power Supply"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("Charge Limit Enforcement"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("Discharge Limit Enforcement"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("Charger Safety Relay"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("Internal Memory"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("Internal Thermistor"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        case("Internal Logic"):
                          $("#f".concat(fstr, "list")).append("BMS Fault");
                          break;

                        default:
                          $("#f".concat(fstr, "list")).append("No information available.");
                      }
                    }
                  };
                }
          });

          setTimeout(arguments.callee, 2000);
      });
