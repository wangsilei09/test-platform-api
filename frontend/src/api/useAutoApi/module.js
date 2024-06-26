import request from '/@/utils/request';

/**
 * 项目使用接口
 * @method getProjectList 获取项目列表
 * @method getMenuTest 获取后端动态路由菜单(test)
 */
export function useModuleApi() {
  return {
    getList: (data) => {
      return request({
        url: '/module/list',
        method: 'POST',
        data,
      });
    },
    getAll: (data) => {
      return request({
        url: '/module/getAllModule',
        method: 'POST',
        data,
      });
    },
    saveOrUpdate(data) {
      return request({
        url: '/module/saveOrUpdate',
        method: 'POST',
        data
      })
    },
    deleted: (data) => {
      return request({
        url: '/module/deleted',
        method: 'POST',
        data,
      });
    },
  };
}
