import { takeLatest, takeEvery, call, put} from 'redux-saga/effects'

function* login({ username, password }) {

}

export function* watchAuth() {
  yield takeLatest('APP:LOGIN', login)
}
