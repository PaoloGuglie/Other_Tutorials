import SearchBar from "./SearchBar.jsx";
import AddItem from "./AddItem.jsx";
import ItemsDisplay from "./ItemsDisplay.jsx";
import Test from "./Class.jsx";

import { useState, useEffect } from "react";

function App()
{
  const [filters, setFilters] = useState({});

  const [data, setData] = useState({items: []});

  const [showTest, setShowTest] = useState(true);

  // Works with the App() component.
  // I can decide when this function runs using a dependency list.
  // If I pass an empty list, the useEffect() function will run only when
  // the component mounts.
  // If the list has items, the useEffect() function will also run when the
  // item changes its value.
  useEffect(() => {
    console.log("Use effect!");

    // "return" will run a function when the component unmounts or when an item
    // changes value. Can be used to clean up the code.
    return() =>
    {
      console.log("Cleanup!");
    }

    // I can run useEffect when I subscribe to a channel. Then, if I decide to
    // unsubscribe, the cleanup "return" function can send the data to the server
    // to unsubscribe me.
    // Then, I can subscribe again. I clean up the previus effect.
  }, []);

  useEffect(() => { console.log("Second useEffect() !") });

  const updateFilters = searchParams =>
  {
    setFilters(searchParams);
  };

  const filterData = data =>
  {
    const filteredData = [];

    // Check if there are filters in place:
    if (!filters.name && !filters.price && !filters.type && !filters.brand)
    {
      return data;
    }

    for (const item of data)
    {
      // Skip the items that do not meet the criteria:

      if (filters.name !== '' && item.name !== filters.name)
      {
        continue;  // skip the item and don't add it to the filtered data.
      }

      if (filters.price !== 0 && item.price > filters.price)
      {
        continue;  // I am above max price, so I skip.
      }

      if (filters.type !== '' && item.type !== filters.type)
      {
        continue;  // same as first
      }

      if (filters.brand !== '' && item.brand !== filters.brand)
      {
        continue;  // same as first
      }

      // If all checks are passed:
      filteredData.push(item);
    }

    return filteredData;
  }

  const addItem = item =>
  {
    // Restore the state into a variable:
    let items = data['items'];

    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(item)
    };

    // The difference betweeen item and data is that, after entering the database, the
    // item receives an ID by it, so I got it back from the database and added it to
    // my items list.

    fetch("http://localhost:3000/items", requestOptions)
    .then(response => response.json)
    .then(data => {
      items.push(data); setData({items: items})
    });
  };

  return (
  <div className="container">
    <div className="row mt-3">
      <ItemsDisplay items={filterData(data['items'])} />
    </div>
    <div className="row mt-3">
      <SearchBar updateSearchParams={updateFilters} />
    </div>
    <div className="row mt-3">
      <AddItem addItem={addItem} />
    </div>
    {showTest ? <Test setShowTest={setShowTest}/> : null}
  </div>);
}

export default App;