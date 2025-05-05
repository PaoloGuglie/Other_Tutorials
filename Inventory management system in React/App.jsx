import SearchBar from "./SearchBar.jsx";
import AddItem from "./AddItem.jsx";
import ItemsDisplay from "./ItemsDisplay.jsx";

import { useState } from "react";

function App()
{
  const [filters, setFilters] = useState({});

  const [data, setData] = useState({items: []});

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
        continue;  // same as the first if statement.
      }

      if (filters.brand !== '' && item.brand !== filters.brand)
      {
        continue;  // same as the first statement.
      }

      // If all checks are passed (otherwise this statement is skipped):
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
  </div>);
}

export default App;
