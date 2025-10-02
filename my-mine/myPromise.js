const PENDING = "pending";
const FULFILLED = "fulfilled";
const REJECTED = "rejected";

class MyPromise {
  state = PENDING;
  result;
  #handlers = []; // [{onFulFilled, onRejected}]

  constructor(func) {
    const resolve = (result) => {
      if (this.state === PENDING) {
        this.state = FULFILLED;
        this.result = result;
        // 支持异步和多次调用
        this.#handlers.forEach(({ onFulfilled }) => {
          onFulfilled(this.result);
        });
      }
    };
    const reject = (result) => {
      if (this.state === PENDING) {
        this.state = REJECTED;
        this.result = result;
        this.#handlers.forEach(({ onRejected }) => {
          onRejected(this.result);
        });
      }
    };
    // 处理实例化异常
    try {
      func(resolve, reject);
    } catch (error) {
      reject(error);
    }
  }

  then(onFulfilled, onRejected) {
    onFulfilled = typeof onFulfilled === "function" ? onFulfilled : (x) => x;
    onRejected =
      typeof onRejected === "function"
        ? onRejected
        : (x) => {
            throw x;
          };
    // 支持链式调用 创建 Promise 的回调函数是立即执行的
    const promise = new MyPromise((resolve, reject) => {
      if (this.state === FULFILLED) {
        runAsyncTask(() => {
          try {
            const x = onFulfilled(this.result);
            resolvePromise(promise, x, resolve, reject);
          } catch (error) {
            reject(error);
          }
        });
      } else if (this.state === REJECTED) {
        runAsyncTask(() => {
          try {
            const x = onRejected(this.result);
            resolvePromise(promise, x, resolve, reject);
          } catch (error) {
            reject(error);
          }
        });
      } else if (this.state === PENDING) {
        this.#handlers.push({
          onFulfilled: () => {
            runAsyncTask(() => {
              try {
                const x = onFulfilled(this.result);
                resolvePromise(p2, x, resolve, reject);
              } catch (error) {
                reject(error);
              }
            });
          },
          onRejected: () => {
            runAsyncTask(() => {
              try {
                const x = onRejected(this.result);
                resolvePromise(p2, x, resolve, reject);
              } catch (error) {
                reject(error);
              }
            });
          },
        });
      }
    });
    return promise;
  }

  catch(onRejected) {
    // 内部调用 then
    return this.then(undefined, onRejected);
  }

  finally(onFinally) {
    return this.then(onFinally, onFinally);
  }

  // 静态方法
  // 如果传入的是 Promise 将会直接返回，否则返回兑现的 Promise
  static resolve(value) {
    if (value instanceof MyPromise) {
      return value;
    }
    return new MyPromise((resolve) => {
      resolve(value);
    });
  }

  // 直接返回被拒绝的 Promise
  static reject(value) {
    return new MyPromise((_, reject) => {
      reject(value);
    });
  }

  static race(promises) {
    return new MyPromise((resolve, reject) => {
      if (!Array.isArray(promises)) {
        reject(new TypeError("Argument is not iterable"));
      }
      promises.forEach((p) => {
        MyPromise.resolve(p).then(
          (res) => {
            resolve(res);
          },
          (err) => {
            reject(err);
          }
        );
      });
    });
  }

  static all(promises) {
    return new MyPromise((resolve, reject) => {
      if (!Array.isArray(promises)) {
        reject(new TypeError("Argument is not iterable"));
      }
      // 空数组直接兑现
      promises.length === 0 && resolve(promises);

      const results = [];
      let count = 0;
      promises.forEach((p, index) => {
        MyPromise.resolve(p).then(
          (res) => {
            results[index] = res;
            count++;
            count === promises.length && resolve(results);
          },
          (err) => {
            reject(err);
          }
        );
      });
    });
  }

  static allSettled(promises) {
    return new MyPromise((resolve, reject) => {
      if (!Array.isArray(promises)) {
        reject(new TypeError("Argument is not iterable"));
      }
      // 空数组直接兑现
      promises.length === 0 && resolve(promises);

      const results = [];
      let count = 0;
      promises.forEach((p, index) => {
        MyPromise.resolve(p).then(
          (res) => {
            results[index] = { status: FULFILLED, value: res };
            count++;
            count === promises.length && resolve(results);
          },
          (err) => {
            results[index] = { status: REJECTED, reason: err };
            count++;
            count === promises.length && resolve(results);
          }
        );
      });
    });
  }

  static any(promises) {
    return new MyPromise((resolve, reject) => {
      if (!Array.isArray(promises)) {
        reject(new TypeError("Argument is not iterable"));
      }
      // 空数组直接拒绝
      promises.length === 0 &&
        reject(new AggregateError(promises, "All promises were rejected"));

      const errors = [];
      let count = 0;
      promises.forEach((p, index) => {
        MyPromise.resolve(p).then(
          (res) => {
            resolve(res);
          },
          (err) => {
            errors[index] = err;
            count++;
            count === promises.length &&
              reject(new AggregateError(errors, "All promises were rejected"));
          }
        );
      });
    });
  }
}

// 开启异步任务
function runAsyncTask(callback) {
  if (typeof queueMicrotask === "function") {
    queueMicrotask(callback);
  } else if (typeof MutationObserver === "function") {
    const obs = new MutationObserver(callback);
    const divNode = document.createElement("div");
    obs.observe(divNode, { childList: true });
    divNode.innerText = "rico";
  } else {
    setTimeout(callback, 0);
  }
}

function resolvePromise(promise, x, resolve, reject) {
  // 处理循环引用
  if (x === promise) {
    throw new TypeError("Chaining cycle detected for promise #<Promise>");
  }
  // 处理返回 Promise 的逻辑
  if (x instanceof MyPromise) {
    x.then(
      (res) => resolve(res),
      (err) => reject(err)
    );
  } else {
    resolve(x);
  }
}
