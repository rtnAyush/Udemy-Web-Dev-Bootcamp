import { legacy_createStore as createStore } from "redux";
import allReducers from "./reducers/index";

const store = createStore(
    allReducers,
);

export default store;