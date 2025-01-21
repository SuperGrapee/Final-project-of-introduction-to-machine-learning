from PyPDF2 import PdfMerger

# 创建 PdfMerger 对象
merger = PdfMerger()

# 添加两个 PDF 文件
merger.append("37245056_TongLuyangyu_FinalReport.pdf")
merger.append("Stress_Image_Classificatioin.pdf")

# 保存合并后的 PDF 文件
merger.write("merged_output.pdf")
merger.close()

print("PDF 文件已合并完成！")