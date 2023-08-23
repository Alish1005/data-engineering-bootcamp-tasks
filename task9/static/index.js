document.addEventListener("DOMContentLoaded", function() {
console.log("1");
});

/*
fetch( '../output.json' )
      .then((res)=>res.json())
      .then((data) => {
      console.log(data)
      });

const ctx = document.getElementById('myChart');
const btn=document.getElementById('info');
    const data=btn.getAttribute('data-info')
    console.log(data)
    new Chart(ctx, {
    type: 'bar',
    data: {
      //labels: Object.keys(data),
      labels: ['cars','vans','SUV','Motorcycle','planes'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });