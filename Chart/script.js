// import DataFrame from 'dataframe-js';

const DataFrame = dfjs.DataFrame;

DataFrame.fromCSV('df_vitals.csv').then(df => {
 
  dfuuid = df.filter(row => row.get('patient_uuid') == 73939445); // 73939445  //82591262 //94488470
  console.log(dfuuid.count());
  dfuuid = dfuuid.head();
  
  var df_dates = dfuuid.toArray('timestamp'); //var ts = df.select('timestamp');
  var df_hr = dfuuid.toArray('HR'); //var ts = df.select('timestamp');
  var df_sbp = dfuuid.toArray('SBP'); //var ts = df.select('timestamp');
  var df_dbp = dfuuid.toArray('DBP'); //var ts = df.select('timestamp');

  console.log(df_dates);

  var ctx = document.getElementById("myChart");
  var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: df_dates, // labels: df.select('timestamp'),  //     
    datasets: [
      { 
        data: df_hr,
        label: "Heart rate",
        borderColor: "#8e5ea2",
        fill: false
      },
      { 
        data: df_sbp,
        label: "Systolic blood pressure",
        borderColor: "#3cba9f",
        fill: false
      },
      { 
        data: df_dbp,
        label: "Diastolic blood pressure",
        borderColor: "#e8c3b9",
        fill: false
      }
    ]
  }
  });

});


