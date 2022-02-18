def solution(id_list, report, k):
    report_dict = {x: set() for x in id_list}   # key: 경고받은id, val: 신고한id
    answer = [0]*len(id_list)

    for r in report:
        id, w_id = r.split()
        report_dict[w_id].add(id)
    
    for id in id_list:
        if len(report_dict[id]) >= k:
            for j in range(len(id_list)):
                if id_list[j] in report_dict[id]:
                    answer[j] += 1
    return answer