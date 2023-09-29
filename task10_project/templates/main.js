 fetch('/data')
      .then((res)=>res.json())
      .then((data) => {
      const top_type=document.getElementById('top-news-type');
      console.log(data)
      d=data[0]
      console.log(Object.keys(d))

      const ctx = document.getElementById('myChart1');
      //I use news.date.split(' ')[0]  only to remove the time from the label
      const dates=[...new Set(data.map(news => news.date.split(' ')[0]))].sort().slice(-75);
      const dates_num=[];
      dates.forEach(i => {
        const t=[...new Set(data.filter(news => news.date.split(' ')[0]==i))];
        dates_num.push(t.length)
       });
       console.log(dates_num)
      console.log(dates_num)
      const types=[...new Set(data.filter(news => dates.includes(news.date.split(' ')[0])).map(news => news.type))];
      const types_num=[];
      types.forEach(i => {
        const t=[...new Set(data.filter(news => news.type==i))];
        types_num.push(t.length)
       });
      console.log(types);
      console.log(types_num);


      const topics=[...new Set(data.filter(news => dates.includes(news.date.split(' ')[0]) && news.type!="program").map(news => news.topic))];
      const topics_num=[]
       topics.forEach(i => {
        const t=[...new Set(data.filter(news => news.topic==i))];
        topics_num.push(t.length)
       });
      console.log(topics);

      console.log(dates);

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: types,
      datasets: [{
        label: ' ',
        data: types_num,
        borderWidth: 1
      }]
    },
    options: {
     plugins: {
            title: {
                display: true,
                text: 'Number of news type'
            }
        },
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
const ctx2 = document.getElementById('myChart2');
  new Chart(ctx2, {
    type: 'bar',
    data: {
      labels: topics,
      datasets: [{
        label: ' ',
        data: topics_num,
        borderWidth: 1
      }]
    },
    options: {
     plugins: {
            title: {
                display: true,
                text: 'Number of news topics'
            }
        },
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });


const ctx3 = document.getElementById('myChart3');
new Chart(ctx3, {
    type: 'line',
    data: {
      labels: dates,
      datasets: [{
        label: ' ',
        data: dates_num,
        borderWidth: 1,
        visible:false
      }]
    },
    options: {
     plugins: {
            title: {
                display: true,
                text: 'Number of daily news last 75 days'
            }
        },
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

    });