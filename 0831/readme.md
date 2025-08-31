# Matplotlib

## 折線圖

### color 
設定折線顏色，可使用顏色名稱或16進位，也可使用顏色縮寫
### linewidth
設定 折線寬度
### linestyle 
設定折線樣式

| 樣式 |  說明  |
|:----:|:------:|
|  -   |  實線  |
|  --  |  虛線  |
|  -.  | 虛點線 |
|  :   | 點狀線 |

### marker 標記
|   樣式    |  說明  |
|:-------:|:------:| 
|    o    |   圓   |
|    .    |   點   |
|    *    |   星   |
|    +    |  十字  |
|    x    |  叉叉  |
|    _    |  橫線  |
|   \|    | 直線 |
| ^,v,<,> | 三角形 |
|    s    |  矩形  |
|    p    | 五邊形 |
|   h,H   | 六邊形 |
|   d,D   |  鑽型  |
| 1,2,3,4 | 人字形 |
### markersize 
標記大小
### markerfacecolor
標記顏色
### markeredgecolor
標記邊框顏色
### markeredgesize 
定義標記邊框大小
### label 圖例說明


## lim & ticks 上下限與刻度
### lim
設定刻度上下限
```python
plt.xlim()
plt.ylim()
```
### ticks
設定刻度。
```python
plt.xticks([1,2,3,4,5])
plt.yticks(range(0,50))
```
> ticks內要設定list或可迭代資料

## title 圖表標題
### 設定中文
預設沒有中文顯示，要將字體設定為預設中文字體，才可以正常顯示中文
```python
plt.rc('font',family='Microsoft Jhenghei')
```

### 設定標題
```python
plt.title('圖表標題')
```
## label 標籤
設定圖表標記
```python
plt.xlabel('日期')
plt.ylabel('溫度')

```