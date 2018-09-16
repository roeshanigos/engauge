<!DOCTYPE html>
<html>
    <head>
        <title>EnGAUGE the Audience!</title>
    </head>
    <body>
        <div id="container" style="min-width: 1000px; height: 800px; margin: 0 auto"></div>
        
        
        <button onclick="showNext();">Next keyword</button>
        
        
        <script src="https://code.highcharts.com/highcharts.js"></script>
        <script src="https://code.highcharts.com/modules/exporting.js"></script>
        <script src="https://code.highcharts.com/modules/export-data.js"></script>
        
        <script>
        
            var chart = Highcharts.chart('container', {
                chart: {
                    type: 'areaspline'
                },
                title: {
                    text: 'Average fruit consumption during one week'
                },
                legend: {
                    layout: 'vertical',
                    align: 'left',
                    verticalAlign: 'top',
                    x: 150,
                    y: 100,
                    floating: true,
                    borderWidth: 1,
                    backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
                },
                xAxis: {
                    plotBands: [
                        <?php
                        function stringToColor($str) {
                            $unique = hexdec(bin2hex($str));
                            
                            return "color: 'rgba(68, " . substr($unique, 3, 2) . ", 213, .2)'";
                            
                        }
                        
                        
                        function getPlotBands() {
                            $bands = array();
                            
                            $files = array_diff(scandir("keywords"), array('.', '..'));
                            
                            // var_dump($files);
                        
                            $count = 0;
                        
                            foreach($files as $file) {
                                $count++;
                                
                                $handle = fopen("keywords/" . $file, "r");
                                if ($handle) {
                                    while (($line = fgets($handle)) !== false) {
                                        $parts = explode(" ", $line);
                                        $startSeconds = $parts[0];
                                        $endSeconds = $parts[1];
                                        $endSeconds = trim(preg_replace('/\s\s+/', ' ', $endSeconds));
                                        $keyword = preg_replace('/\\.[^.\\s]{3,4}$/', '', $file);
                                        array_push($bands, "{id: '" . $count . "" . "', from: " . $startSeconds . ", to: " . $endSeconds . ", " . stringToColor($keyword) . ", label: { text: '" . $keyword . "' }},");
                                    }
                                
                                    fclose($handle);
                                } else {
                                    // error opening the file.
                                }
                            }
                            
                            return $bands;
                        }
                        
                        
                            $bands = getPlotBands();
                            
                            
                            // var_dump($bands);
                        
                            foreach($bands as $band) {
                                echo $band . "\n";
                            }
                        ?>
                    ]
                },
                yAxis: {
                    title: {
                        text: 'Engagement'
                    }
                },
                tooltip: {
                    shared: true,
                    valueSuffix: ' units'
                },
                credits: {
                    enabled: false
                },
                plotOptions: {
                    areaspline: {
                        fillOpacity: 0.5
                    }
                },
                series: [{
                    name: 'Audience engagement',
                    data: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                }]
            });
            
            
            for (var i = 0; i < <?php echo sizeof($bands); ?>; i++) {
                chart.xAxis[0].removePlotBand((1 + i) + '');
            }
            
            
            <?php
            $js_array = json_encode($bands);
            echo "var bands = ". $js_array . ";\n";
            ?>
            
            
            function between(string, a, b) {
                return string.split(a).pop().split(b).shift();
            }
            
            
            var current = 0;
            
            function showNext() {
                chart.xAxis[0].removePlotBand('cool-band');
                currentLabel = between(bands[current + 1], 'label: { text: \'', '\' }},');
                
                while(true) {
                    if (between(bands[current + 1], 'label: { text: \'', '\' }},') != currentLabel) {
                        break;
                    }
                    
                    chart.xAxis[0].addPlotBand({
                        from: between(bands[current + 1], 'from: ', ', to: '),
                        to: between(bands[current + 1], ', to: ', ', color: '),
                        color: 'rgba(30, 14, 213, .4)',
                        label: { text: currentLabel },
                        id: 'cool-band'
                    });
                    
                    current++;
                    current = current % <?php echo sizeof(array_diff(scandir("keywords"), array('.', '..'))); ?>;
                }
            }
        </script>
    </body>
</html>