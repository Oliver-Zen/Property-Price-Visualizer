# USA-Property-Price-Visualization

## Steps to Run the Visualization Demo Locally

- Download two missing GeoJSON files from https://github.com/OpenDataDE/State-zip-code-GeoJSON due to file size limit of GitHub Enterprise.
  - ca_california_zip_codes_geo.min.json
  - tx_texas_zip_codes_geo.min.json
- Place them in the GeoJSON directory.
- Open a terminal window.
- Navigate to the project directory.
- Run the command 'python -m http.server 8000' to start the local server.
- Open a web browser at http://localhost:8000/.
- Open and run "visualization_v4.html".

## Implemented Functionalities

### Front End [Dongsheng Yao]

- Select between radio options to swith between USA choropleth map based on median property price and number of listing by state.
- Drag a state from the USA choropleth map to the right-top area of the page, a separate state map (breakdown by zipcode) will be generated for visualization. We currently only support to visualize median price by each zipcode area.
- Both USA and state map will show detail information via a orange tooltip when moveing the cursor of mouse over a state/zipcode.
- Drag a state from the USA choropleth map to the right-top area of the page will also generate a multi-dimensional view plot at the right-down area of the page. When moving the cursor through different zipcode areas, the corresponding line from the multi-dimensional view plot will be highlighted in orange color.
- We can visualize a differnt state by simply dragging it to the right-top area to replace the current map.
- Notes #1: The current implementation fetches all the geojson data when running for the first time, so it may take several seconds to load the state map.
- Notes #2: Dragging a zipcode area from the state map to the left-down area of the page will pass all the data to it for future functionalities (it only console.log the data currently.)

## TODO List

- Optional: Add necessary new visualization plot to the left-down area by taking advantage of the drag-and-pass features.
- Implement backend to integrate machine learning models for prediction. [Linhao Bai]
- Incorporate LLM models to generate summaries from the existing visualization. [Yupeng Tang and/or Xianrui Teng]
- Design poster. [To be assigned to the person who will be available when others are working on the assigned tasks.]
- Final report. [Ian Wong: Focus on 'Experiments/ Evaluation' part; Dongsheng Yao: Refine 'Method' part.]
