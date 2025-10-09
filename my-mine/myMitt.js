/**
 * @callback TCallback
 * @param {...unknown} args
 * @returns {void}
 */

class MyMitt {
  constructor() {
    /**
     * @type {Map<string, Set<TCallback>}
     */
    this.core = new Map();
  }

  /**
   *
   * @param {string} type
   * @param {TCallback} callback
   */
  on(type, callback) {
    if (this.core.has(type)) {
      this.core.get(type).add(callback);
    } else {
      this.core.set(type, new Set([callback]));
    }
  }

  /**
   *
   * @param {string} type
   * @param {TCallback} callback
   */
  off(type, callback) {
    if (this.core.has(type)) {
      this.core.get(type).delete(callback);
      if (this.core.get(type).size === 0) {
        this.core.delete(type);
      }
    }
  }

  /**
   *
   * @param {string} type
   * @param  {...unknown} args
   */
  emit(type, ...args) {
    if (this.core.has(type)) {
      this.core.get(type).forEach((callback) => callback(...args));
    }
  }

  /**
   *
   * @param {type} type
   * @param {TCallback} callback
   */
  once(type, callback) {
    const wrappedCallback = (...args) => {
      callback(...args);
      this.off(type, wrappedCallback);
    };
    this.on(type, wrappedCallback);
  }

  clear() {
    this.core.clear();
  }
}

export const mitt = new MyMitt();
