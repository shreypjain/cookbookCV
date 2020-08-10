//
//  RecipeViewController.swift
//  cookbookCV
//
//  Created by Shrey Jain on 8/9/20.
//  Copyright © 2020 Shrey Jain. All rights reserved.
//

import UIKit

class RecipeViewController: UIViewController {
    
    
    @IBOutlet weak var tableView: UITableView!
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemTeal
        configureTableView()
        // Do any additional setup after loading the view.
    }
    
    func configureTableView() {
        view.addSubview(tableView)
        settableViewDelegates()
        tableView.rowHeight = 100
        //register cells
        tableView.register(RecipeCell.self, forCellReuseIdentifier: "RecipeItem")
        //set constraints
    }
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */
    func settableViewDelegates() {
        tableView.delegate = self
        tableView.dataSource = self
    }

}
extension RecipeViewController: UITableViewDelegate, UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 10
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "RecipeItem") as! RecipeCell
        
        return cell
    }
    
    
}

