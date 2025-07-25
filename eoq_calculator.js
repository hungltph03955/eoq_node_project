const { ChartJSNodeCanvas } = require('chartjs-node-canvas');

// Dữ liệu từ bài toán
const D = 1040; // Nhu cầu hàng năm (20 chiếc/tuần × 52 tuần)
const S = 60;   // Chi phí đặt hàng mỗi lần (USD)
const H = 25;   // Chi phí lưu kho mỗi chiếc mỗi năm (25% × 100 USD)

// Tạo mảng số lượng đặt hàng (bước nhảy nhỏ hơn để mượt mà)
const Q = [];
for (let i = 50; i <= 1000; i += 5) Q.push(i); // Bước 5 để biểu đồ mượt hơn

// Tính toán chi phí (không ceil để khớp lý thuyết)
const orderingCost = Q.map(q => (D / q) * S); // Liên tục, không làm tròn
const holdingCost = Q.map(q => (q / 2) * H);
const totalCost = Q.map((q, index) => orderingCost[index] + holdingCost[index]);

// Tính EOQ
const EOQ = Math.sqrt((2 * D * S) / H);
const minTotalCost = (D / EOQ) * S + (EOQ / 2) * H;

// Tìm chỉ số gần nhất của EOQ
const closestQIndex = Q.reduce((closest, current, index) => {
  return Math.abs(current - EOQ) < Math.abs(Q[closest] - EOQ) ? index : closest;
}, 0);
const closestQ = Q[closestQIndex];
const intersectionHoldingCost = holdingCost[closestQIndex];
const intersectionOrderingCost = orderingCost[closestQIndex];

// Cấu hình và vẽ biểu đồ
const width = 1000; // Lớn hơn để dễ nhìn
const height = 700;
const chartCallback = (ChartJS) => {
  ChartJS.defaults.font.size = 16; // Font lớn hơn
  ChartJS.defaults.font.family = 'Arial'; // Font dễ đọc
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
          borderColor: 'rgb(255, 0, 0)', // Đỏ rực
          backgroundColor: 'rgba(255, 0, 0, 0.1)',
          fill: true,
          tension: 0.3, // Làm đường cong mượt hơn
        },
        {
          label: 'Chi phí đặt hàng',
          data: orderingCost,
          borderColor: 'rgb(0, 0, 255)', // Xanh dương nổi
          backgroundColor: 'rgba(0, 0, 255, 0.1)',
          fill: true,
          tension: 0.3,
        },
        {
          label: 'Tổng chi phí',
          data: totalCost,
          borderColor: 'rgb(0, 128, 0)', // Xanh lá
          backgroundColor: 'rgba(0, 128, 0, 0.1)',
          fill: true,
          tension: 0.3,
        },
      ],
    },
    options: {
      scales: {
        x: { 
          title: { display: true, text: 'Số lượng đặt hàng (chiếc)', font: { size: 18 } },
          grid: { lineWidth: 0.5, color: 'rgba(0, 0, 0, 0.1)' } // Lưới mờ
        },
        y: { 
          title: { display: true, text: 'Chi phí (USD)', font: { size: 18 } }, 
          beginAtZero: true,
          grid: { lineWidth: 0.5, color: 'rgba(0, 0, 0, 0.1)' }
        },
      },
      plugins: {
        legend: { 
          position: 'top', 
          labels: { font: { size: 14 }, boxWidth: 20, padding: 20 },
          display: true
        },
        annotation: {
          annotations: [
            {
              type: 'line',
              mode: 'vertical',
              scaleID: 'x',
              value: closestQ,
              borderColor: 'purple',
              borderWidth: 3, // Dày hơn để nổi bật
              label: { 
                content: `EOQ ≈ ${EOQ.toFixed(0)} chiếc (gần ${closestQ})`, 
                enabled: true, 
                position: 'top',
                backgroundColor: 'rgba(128, 0, 128, 0.8)', // Nền tím mờ
                font: { size: 14 }
              },
            },
            {
              type: 'point',
              xValue: closestQ,
              yValue: intersectionHoldingCost,
              backgroundColor: 'purple',
              radius: 8, // To hơn
              label: { 
                content: `Giao điểm lưu kho ≈ ${intersectionHoldingCost.toFixed(0)} USD`, 
                enabled: true, 
                position: 'right',
                backgroundColor: 'white',
                font: { size: 12 }
              },
            },
            {
              type: 'point',
              xValue: closestQ,
              yValue: intersectionOrderingCost,
              backgroundColor: 'purple',
              radius: 8,
              label: { 
                content: `Giao điểm đặt hàng ≈ ${intersectionOrderingCost.toFixed(0)} USD`, 
                enabled: true, 
                position: 'left',
                backgroundColor: 'white',
                font: { size: 12 }
              },
            },
            {
              type: 'line',
              mode: 'horizontal',
              scaleID: 'y',
              value: minTotalCost,
              borderColor: 'orange',
              borderWidth: 2,
              label: { 
                content: `Tổng chi phí tối thiểu ≈ ${minTotalCost.toFixed(0)} USD`, 
                enabled: true, 
                position: 'left',
                backgroundColor: 'rgba(255, 165, 0, 0.8)',
                font: { size: 14 }
              },
            },
          ],
        },
      },
      elements: {
        line: { borderWidth: 2 } // Độ dày đường
      },
      layout: { padding: 20 } // Khoảng cách viền
    },
  };

  const image = await chartJSNodeCanvas.renderToBuffer(configuration);
  require('fs').writeFileSync('eoq_chart.png', image);

  console.log(`Chi phí tồn kho với 400 chiếc: ${(D / 400 * S * Math.ceil(D / 400) + (400 / 2) * H).toFixed(0)} USD`);
  console.log(`Chi phí tồn kho với 500 chiếc: ${(D / 500 * S * Math.ceil(D / 500) + (500 / 2) * H).toFixed(0)} USD`);
})();