const { ChartJSNodeCanvas } = require('chartjs-node-canvas');

// Dữ liệu từ bài toán
const D = 1040; // Nhu cầu hàng năm (20 chiếc/tuần × 52 tuần)
const S = 60;   // Chi phí đặt hàng mỗi lần (USD)
const H = 25;   // Chi phí lưu kho mỗi chiếc mỗi năm (25% × 100 USD)

// Tạo mảng số lượng đặt hàng 
const Q = [];
for (let i = 50; i <= 1000; i += 10) Q.push(i);
// cái cây này đang mô phỏng việc số lượng đặt hàng thay đổi không chỉ là 400 chiếc theo như bài mà còn nhiều trường hợp nữa 
// có thể mo phỏng bài toán nhập 400 chiếc như sau 
// const Q = [400]
// console.log("Q___11 : ", Q);

// Tính toán chi phí
const orderingCost = Q.map(q => (D / q) * S * Math.ceil(D / q)); // Chi phí đặt hàng
const holdingCost = Q.map(q => (q / 2) * H);                   // Chi phí lưu kho
const totalCost = Q.map((q, index) => orderingCost[index] + holdingCost[index]); // Tổng chi phí

// Tính EOQ
const EOQ = Math.sqrt((2 * D * S) / H);

// console.log("EOQ_111 : ", EOQ);

const minTotalCost = (D / EOQ) * S + (EOQ / 2) * H;

// Cấu hình và vẽ biểu đồ
const width = 800;
const height = 600;
const chartCallback = (ChartJS) => {
  ChartJS.defaults.font.size = 14;
};

const chartJSNodeCanvas = new ChartJSNodeCanvas({ width, height, chartCallback });

(async () => {
    const configuration = {
      type: 'line',
      data: {
        labels: Q,
        datasets: [
          {
            label: 'Chi phí lưu kho',
            data: holdingCost,
            borderColor: 'rgb(255, 99, 132)',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            fill: true,
          },
          {
            label: 'Chi phí đặt hàng',
            data: orderingCost,
            borderColor: 'rgb(54, 162, 235)',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            fill: true,
          },
          {
            label: 'Tổng chi phí',
            data: totalCost,
            borderColor: 'rgb(75, 192, 192)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            fill: true,
          },
        ],
      },
      options: {
        scales: {
          x: { title: { display: true, text: 'Số lượng đặt hàng (chiếc)' } },
          y: { title: { display: true, text: 'Chi phí (USD)' }, beginAtZero: true },
        },
        plugins: {
          legend: { position: 'top' },
          annotation: {
            annotations: [
              {
                type: 'line',
                mode: 'vertical',
                scaleID: 'x',
                value: EOQ,
                borderColor: 'red',
                borderWidth: 2,
                label: { content: `EOQ ≈ ${EOQ.toFixed(0)} chiếc`, enabled: true },
              },
              {
                type: 'line',
                mode: 'horizontal',
                scaleID: 'y',
                value: minTotalCost,
                borderColor: 'green',
                borderWidth: 2,
                label: { content: `Tổng chi phí tối thiểu ≈ ${minTotalCost.toFixed(0)} USD`, enabled: true },
              },
            ],
          },
        },
      },
    };
  
    const image = await chartJSNodeCanvas.renderToBuffer(configuration);
    require('fs').writeFileSync('eoq_chart.png', image);
  
    console.log(`Chi phí tồn kho với 400 chiếc: ${(D / 400 * S * Math.ceil(D / 400) + (400 / 2) * H).toFixed(0)} USD`);
    console.log(`Chi phí tồn kho với 500 chiếc: ${(D / 500 * S * Math.ceil(D / 500) + (500 / 2) * H).toFixed(0)} USD`);
  })();